from kafka import KafkaConsumer
consumer = KafkaConsumer(bootstrap_servers='localhost:9092')
consumer.subscribe(['TopicIn'])

for msg in consumer:
    print(msg)