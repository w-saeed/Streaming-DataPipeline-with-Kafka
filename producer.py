import time
import json
import random
from datetime import datetime
from data_generator import generate_message
from kafka import KafkaProducer


# Messages will be serialized as JSON
def serializer(message):
    return json.dumps(message).encode('utf-8')


# Kafka Producer
producer = KafkaProducer(
    bootstrap_servers=['localhost:29092'],
    value_serializer=serializer
)

if __name__ == '__main__':
    while True:
        # Generate a message
        dummy_message = generate_message()
        print(type(dummy_message))
        # Send to topic
        print(
            f'Producing message @ {datetime.now()} | Message = {str(dummy_message)}')
        producer.send('messages', dummy_message)

        # sleep time
        time_to_sleep = random.randint(1, 11)
        time.sleep(time_to_sleep)
