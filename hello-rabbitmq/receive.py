import pika


def mycallback(ch, method, properties, body):
    print(f" [x] Received {body}")
    ch.basic_ack(delivery_tag=method.delivery_tag)


broker_param = pika.ConnectionParameters('localhost')
connection = pika.BlockingConnection(broker_param)
channel = connection.channel()

channel.queue_declare(queue='myqueue', durable=True)

channel.basic_consume(
    queue='myqueue',
    on_message_callback=mycallback,
    auto_ack=False,
)

print(' [*] Waiting for messages. To exit press CTRL+C')
channel.start_consuming()
