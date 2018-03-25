import time
import json
import datetime
import Adafruit_DHT
from kafka import KafkaProducer


producer = KafkaProducer(bootstrap_servers='kafka1:9614', value_serializer=lambda v: json.dumps(v).encode('utf-8'), request_timeout_ms=10000)

while True:
    humidity, temperature = Adafruit_DHT.read_retry(22, 22)
    producer.send('temphum', {'temp': temperature, 'hum': humidity, 'wkt': str(datetime.datetime.now())})
    time.sleep(5)
