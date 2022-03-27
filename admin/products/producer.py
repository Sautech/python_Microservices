import pika

params = pika.URLParameters('amqps://ipzsixlh:sSgSqbVBVew8EHtaBW8kMpqW6tPkQdtZ@puffin.rmq2.cloudamqp.com/ipzsixlh')

connection = pika.BlockingConnection(params)

channel = connection.channel()

def publish():
    channel.basic_publish(exchange='', routing_key='admin', body='hello')

