#Maggie Lu
#CS 336 - Computer Network
#Final Project - Messages Broadcasting
#May 09 2018

import pika
import sys

url = "YourOwnUrl" ;
params = pika.URLParameters(url);
connection = pika.BlockingConnection(params)

channel = connection.channel()

channel.exchange_declare(exchange='logs',
                         exchange_type='fanout')

message = ' '.join(sys.argv[1:]) or "info: Hello World!"
channel.basic_publish(exchange='logs',
                      routing_key='',
                      body=message)
print(" [x] Sent %r" % message)
connection.close()