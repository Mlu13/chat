#Maggie Lu
#CS 336 - Computer Network
#Final Project - Messages Broadcasting
#May 09 2018

import pika

url = "YourOwnUrl" ;
params = pika.URLParameters(url);
connection = pika.BlockingConnection(params)
channel = connection.channel()

channel.exchange_declare(exchange='logs',
                         exchange_type='fanout')

result = channel.queue_declare(exclusive=True)
queue_name = result.method.queue

channel.queue_bind(exchange='logs',
                   queue=queue_name)

print(' [*] Waiting for logs. To exit press CTRL+C')

def callback(ch, method, properties, body):
    print(" [x] %r" % body)

channel.basic_consume(callback,
                      queue=queue_name,
                      no_ack=True)

channel.start_consuming()