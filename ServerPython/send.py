#!/usr/bin/env python
import pika, os

# Access the CLOUDAMQP_URL enviroment variable and parse ir (fallback  to localhost)
url = os.environ.get('CLOUDAMQP_URL', 'amqps://ncfriifr:qBs9huQiE-n2IT8ksjYPsL9-kt6Vj-T_@jackal.rmq.cloudamqp.com/ncfriifr')
params = pika.URLParameters(url)
connection = pika.BlockingConnection(params)
channel = connection.channel() # start a channel
channel.queue_declare(queue='hello') # Declare a queue
channel.basic_publish(exchange='',
                      routing_key='hello',
                      body='10')

print(" [x] Enviando 'Nota [10] para o Ana Carolina Felicio e Guilherme Vilela' ")
connection.close()
