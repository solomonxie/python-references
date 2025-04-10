import pika
from random import randint

broker_param = pika.ConnectionParameters('localhost')
connection = pika.BlockingConnection(broker_param)
channel = connection.channel()
_ = channel.queue_declare(queue='myqueue', durable=True)

resp = channel.basic_publish(
    exchange='',
    routing_key='myqueue',
    body=f'Hello World! ({randint(1, 100)})',
)

connection.close()
print(" [x] Sent 'Hello World!'")
