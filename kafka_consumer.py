"""                                               
  ___ ___  _ __  ___ _   _ _ __ ___   ___ _ __ 
 / __/ _ \| '_ \/ __| | | | '_ ` _ \ / _ \ '__|
| (_| (_) | | | \__ \ |_| | | | | | |  __/ |   
 \___\___/|_| |_|___/\__,_|_| |_| |_|\___|_|   
"""

from kafka import KafkaConsumer

consumer = KafkaConsumer(
        'my_favorite_topic', bootstrap_servers=['localhost:9093'])

print("Consuming messages")
for msg in consumer:
    print(msg)
