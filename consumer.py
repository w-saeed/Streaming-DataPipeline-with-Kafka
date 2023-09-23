import json
from kafka import KafkaConsumer
import db


if __name__ == '__main__':
    # Kafka Consumer
    consumer = KafkaConsumer(
        'messages',
        bootstrap_servers='localhost:29092',
        auto_offset_reset='latest'
    )
    for message in consumer:
        # print(json.loads(message.value))
        db.save(json.loads(message.value))
