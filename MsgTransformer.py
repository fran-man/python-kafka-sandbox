from kafka import KafkaProducer,KafkaConsumer

prod = KafkaProducer(bootstrap_servers='kafka:9092',max_block_ms=5000)

consumer = KafkaConsumer(bootstrap_servers='kafka:9092')
consumer.subscribe(['TopicIn'])

for msg in consumer:
    future = prod.send('TopicOut', msg.value)
    future.get()