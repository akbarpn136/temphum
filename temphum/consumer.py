import json
from kafka import KafkaConsumer

consumer = KafkaConsumer('temphum', bootstrap_servers='kafka1:9614', value_deserializer=lambda m: json.loads(m.decode('ascii')))

for msg in consumer:
    print(msg.value)
