from kafka import KafkaProducer
prod = KafkaProducer(bootstrap_servers='kafka:9092',max_block_ms=5000)

for i in range(1,11):
    future = prod.send('TopicIn',bytearray('Hello World!','utf8'))
    print("Sent to partition: %s" % future.get().topic_partition.partition)