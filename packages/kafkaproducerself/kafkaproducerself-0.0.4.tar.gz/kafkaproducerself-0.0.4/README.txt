Description:

KafkaProducerSelf is a Python library that offers general functions to interact with Kafka producers and publish events using them. Additionally, it includes a health check feature to ensure the connection is live and working properly.



Installation:

To install KafkaProducerSelf, simply use pip:
pip install kafkaproducerself





Functionality:

The library provides three main functions:

1. 'health_check'

a) Accepts a URL as a parameter.
b) Returns a tuple:
    True/False: Indicates whether the connection is active or not.
    String: Success or failure message.


2. 'connect_to_kafka_producer'

a) Accepts a URL as a parameter.
b) Returns a tuple:
    True/False: Indicates the status of the producer (whether connected or not).
    Obj/String: The producer object if connected successfully; otherwise, an error message.



3. 'push_event_to_kafka'

a) Accepts eventData, topicName, and producer as parameters.
b) Returns a tuple:
    True/False: Indicates if the message was successfully published or not.
    String: Success or failure message.





Usage:

To use the KafkaProducerSelf library, first, make sure it is installed via pip. Then, import the library in your Python script and utilize the provided functions according to your needs.


Example :

import kafkaproducerself

# Perform a health check
url = "kafka://example.com:9092"
health_status, message = kafkaproducerself.health_check(url)
print(f"Health check result: {health_status}. Message: {message}")

# Connect to the Kafka producer
producer_status, producer = kafkaproducerself.connect_to_kafka_producer(url)
if producer_status:
    print("Connected to Kafka producer successfully.")
else:
    print(f"Failed to connect to Kafka producer. Error: {producer}")

# Publish an event to Kafka
event_data = "Hello, Kafka!"
topic_name = "example_topic"
push_status, push_message = kafkaproducerself.push_event_to_kafka(event_data, topic_name, producer)
print(f"Event publication result: {push_status}. Message: {push_message}")
