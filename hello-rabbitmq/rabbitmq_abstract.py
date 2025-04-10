"""
RabbitMQHelper: a small, generic wrapper around RabbitMQ (via `pika`) for
publishing tasks to a queue and consuming them with a worker, plus Redis for
tracking each task's status (QUEUED -> WIP -> DONE/FAILED/EXPIRED).

See README.md in this folder for how to run RabbitMQ/Redis locally and try
this end to end.
"""
import os
import json
import logging
from time import time
from typing import Callable
from functools import partial
from dataclasses import dataclass, asdict, field

import pika
import redis

from reinvent_wheels.builtin.error_utils import retry
from reinvent_wheels.network.socket_utils import get_safe_hostname

logger = logging.getLogger(__name__)

# Unit of time constant here is seconds by default, '_MS' means milliseconds
MESSAGE_TTL_MS = 1000 * 60 * 10
TASK_STATUS_TTL = 60 * 60 * 24
MAX_PROCESS_TIME = 60 * 30
# https://pika.readthedocs.io/en/stable/examples/heartbeat_and_blocked_timeouts.html
# A longer heartbeat than pika's default (60s) lets a long-running consumer keep
# its connection to the broker alive while it's busy processing a task.
HEARTBEAT_TIMEOUT = 60 * 3
BLOCKED_CONNECTION_TIMEOUT = 60 * 5


class TaskStatus:
    QUEUED = 'QUEUED'
    WIP = 'WIP'
    DONE = 'DONE'
    FAILED = 'FAILED'
    EXPIRED = 'EXPIRED'
    NOT_EXISTED = 'NOT_EXISTED'


@dataclass
class TaskBody:
    """Example task payload. Extend/replace with whatever fields your task needs."""
    task_id: str
    payload: dict = field(default_factory=dict)

    def to_json(self) -> str:
        return json.dumps(asdict(self))

    @classmethod
    def from_json(cls, raw) -> 'TaskBody':
        data = json.loads(raw)
        return cls(**data)


def get_rabbitmq_config() -> tuple:
    return (
        os.getenv('RABBITMQ_HOST', 'localhost'),
        int(os.getenv('RABBITMQ_PORT', 5672)),
        os.getenv('RABBITMQ_USERNAME'),
        os.getenv('RABBITMQ_PASSWORD'),
    )


def get_redis_client(db: int = 0) -> redis.Redis:
    return redis.Redis(
        host=os.getenv('REDIS_HOST', 'localhost'),
        port=int(os.getenv('REDIS_PORT', 6379)),
        db=db,
    )


class RabbitMQHelper:

    def __init__(self, queue_name: str, worker_name: str = None):
        self.queue_name = queue_name
        self.worker_name = worker_name or queue_name
        self.hostname = get_safe_hostname()
        host, port, username, password = get_rabbitmq_config()
        credentials = pika.PlainCredentials(username, password) if username else None
        self.broker_parameters = pika.ConnectionParameters(
            host=host,
            port=port,
            credentials=credentials,
            heartbeat=HEARTBEAT_TIMEOUT,
            blocked_connection_timeout=BLOCKED_CONNECTION_TIMEOUT,
        )
        self.connection = pika.BlockingConnection(self.broker_parameters)
        self.channel = self.connection.channel()
        self.channel.queue_declare(queue=self.queue_name, durable=True)
        self.redis = get_redis_client()
        self.debug = {}

    def get_redis_task_key(self, task_id: str) -> str:
        return f'task_status:{self.queue_name}:{task_id}'

    def push_task(self, task_id: str, task_body: TaskBody):
        with pika.BlockingConnection(self.broker_parameters) as conn:
            channel = conn.channel()
            channel.queue_declare(queue=self.queue_name, durable=True)
            channel.basic_publish(
                exchange='', routing_key=self.queue_name,
                # NOTE: Message flow: Producer -> Exchange -> Queue(s) -> Consumer.
                # NOTE: This uses only the default (nameless) exchange to route directly
                # NOTE: to a single queue; swap in a named exchange to fan out to more.
                body=task_body.to_json(),
                properties=pika.BasicProperties(
                    headers={'queue_name': self.queue_name},
                    expiration=str(MESSAGE_TTL_MS),
                ),
            )
            logger.info(f'Published task[{task_id}] to queue[{self.queue_name}]')
        self.set_task_status(task_id, TaskStatus.QUEUED)

    def set_task_status(self, task_id: str, status: str):
        """Redis data structure: key -> [info0, info1, info2, ...]
        infoN = "<hostname>:<epoch_seconds>:<status>"
        """
        task_key = self.get_redis_task_key(task_id)
        is_new_key = not self.redis.exists(task_key)
        self.redis.rpush(task_key, f'{self.hostname}:{int(time())}:{status}')
        if is_new_key:
            self.redis.expire(task_key, TASK_STATUS_TTL)

    def get_task_info(self, task_id: str) -> tuple:
        task_key = self.get_redis_task_key(task_id)
        if not self.redis.exists(task_key):
            return (0, TaskStatus.NOT_EXISTED)
        history = self.redis.lrange(task_key, 0, -1)
        status = history[-1].decode().split(':')[-1]
        created_at = int(history[0].decode().split(':')[1])
        updated_at = int(history[-1].decode().split(':')[1])
        duration = (updated_at - created_at) if len(history) > 1 else int(time() - created_at)
        return (duration, status)

    @retry(errors=(pika.exceptions.ChannelClosedByBroker, pika.exceptions.ConnectionWrongStateError), tries=5, delay=5)
    def listen_queue(self, callback_func: Callable):
        self.channel.basic_qos(prefetch_count=1)  # each worker takes 1 message at a time
        self.channel.basic_consume(
            queue=self.queue_name,
            auto_ack=False,  # must stay False for the retry/requeue logic below to work
            on_message_callback=partial(self.callback_wrap, callback_func),
        )
        self.channel.start_consuming()
        self.channel.close()
        self.connection.close()
        logger.info(f'Worker[{self.worker_name}] connection closed.')

    def callback_wrap(self, callback_func: Callable, channel, method, properties, body):
        logger.debug(f'Starting task: {body}')
        task = TaskBody.from_json(body)
        try:
            duration, status = self.get_task_info(task.task_id)
            if duration > MAX_PROCESS_TIME:
                self.set_task_status(task.task_id, TaskStatus.EXPIRED)
                raise TimeoutError(f'Task[{task.task_id}] stalled at [{status}] for {duration}s')
            self.set_task_status(task.task_id, TaskStatus.WIP)
            callback_func(task)
            self.set_task_status(task.task_id, TaskStatus.DONE)
            channel.basic_ack(delivery_tag=method.delivery_tag)
            # NOTE: RabbitMQ only redelivers a message once the consumer holding it
            # NOTE: disconnects, so it's safe to ack only after the callback finishes.
        except Exception as e:
            logger.exception(e)
            self.set_task_status(task.task_id, TaskStatus.FAILED)
            if channel.is_open:
                # requeue=False: an exception is almost always a code/data bug that a
                # blind retry won't fix, so drop the message instead of looping forever.
                channel.basic_nack(delivery_tag=method.delivery_tag, requeue=False)

    def graceful_shutdown(self, signal_number: int, _):
        logger.info(f'Worker[{self.worker_name}] received signal({signal_number}), shutting down...')
        try:
            self.channel.stop_consuming()  # finish the in-flight message, then stop
        except Exception as e:
            logger.warning(e)
