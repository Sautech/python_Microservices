import pika

params = pika.URLParameters('amqps://ipzsixlh:sSgSqbVBVew8EHtaBW8kMpqW6tPkQdtZ@puffin.rmq2.cloudamqp.com/ipzsixlh')

connection = pika.BlockingConnection(params)

channel = connection.channel()

channel.queue_declare(queue='admin')

def callback(ch, method, properties, body):
    print('Received in admin')
    print(body)

channel.basic_consume(queue='admin', on_message_callback=callback)

print('Started Consuming')
channel.start_consuming()

channel.close()
