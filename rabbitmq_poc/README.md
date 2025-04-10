# RabbitMQ POC

Two flavors of the same idea, from simplest to most complete:

- `send.py` / `receive.py` — the textbook "Hello World" pika producer/consumer,
  talking to a queue directly.
- `rabbitmq_abstract.py` — a reusable `RabbitMQHelper` that wraps that same
  pattern into a small task-queue library: publish a task, track its status
  in Redis (`QUEUED` -> `WIP` -> `DONE`/`FAILED`/`EXPIRED`), and consume with
  a worker loop that handles ack/nack and graceful shutdown for you.

## Run it locally

```sh
# RabbitMQ (management UI at http://localhost:15672, user/pass: guest/guest)
docker run -it --rm --name rabbitmq -p 5672:5672 -p 15672:15672 rabbitmq:3.13-management
# or: server_mac.sh / brew install rabbitmq

# Redis (only needed for rabbitmq_abstract.py's task-status tracking)
docker run --rm --name redis-server -p 6379:6379 redis
```

Install deps: `pip install -r requirements.txt`

### `send.py` / `receive.py`

```sh
python receive.py   # in one terminal
python send.py      # in another; repeat to publish more messages
```

### `rabbitmq_abstract.py`

```python
from rabbitmq_abstract import RabbitMQHelper, TaskBody

helper = RabbitMQHelper(queue_name='demo_queue')

# Producer side:
helper.push_task('task-1', TaskBody(task_id='task-1', payload={'foo': 'bar'}))

# Worker side:
def handle(task: TaskBody):
    print('processing', task)

helper.listen_queue(handle)
```

Environment variables it reads (all optional, shown with their defaults):

```sh
export RABBITMQ_HOST=localhost
export RABBITMQ_PORT=5672
export RABBITMQ_USERNAME=       # unset -> no auth (RabbitMQ's default "guest" account)
export RABBITMQ_PASSWORD=
export REDIS_HOST=localhost
export REDIS_PORT=6379
```

## Production notes

- Check queue depth: `sudo rabbitmqctl list_queues name messages consumers`
- Quick connectivity check:
  ```python
  import pika
  credentials = pika.PlainCredentials(username='myname', password='mypass')
  params = pika.ConnectionParameters(host='rabbitmq.example.com', port=5672, credentials=credentials)
  channel = pika.BlockingConnection(params).channel()
  ```
