import os
import json
from services import LocationService
from kafka import KafkaConsumer


TOPIC_NAME = 'location_topic'
KAFKA_SERVER = 'kafka:9092'


consumer = KafkaConsumer(TOPIC_NAME, bootstrap_servers=KAFKA_SERVER)
for message in consumer:
    location = json.loads(message.value.decode('utf-8'))
    LocationService.create(location)