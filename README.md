# Proof of Concept

Web -- http --> [KrakenD] -> Kafka

## How to run it?
```
# Setup the env
docker-compose up

# make requests
python krakend_producer.py

# check topic
python kafka_consumer.py
```

You might have to create the Topic
```
docker-compose exec kafka bash
/opt/bitnami/kafka/bin/kafka-topics.sh --create --bootstrap-server localhost:9092 --replication-factor 1 --partitions 1 --topic my_favorite_topic
```
