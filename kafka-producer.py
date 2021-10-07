import time
from kafka import KafkaProducer

import json

producer = KafkaProducer(
    value_serializer = lambda m : json.dumps(m).encode('utf-8'),bootstrap_servers=['localhost:9092'])

open_json = open("product-views.json")
read_json = open_json.read()
list_json = read_json.split("\n")

for data in list_json:
    try:
        producer.send("hepsiburada-kafka",value=json.loads(data))
        print("{} is sending to Kafka".format(data))
    except Exception as e:
        print(e)