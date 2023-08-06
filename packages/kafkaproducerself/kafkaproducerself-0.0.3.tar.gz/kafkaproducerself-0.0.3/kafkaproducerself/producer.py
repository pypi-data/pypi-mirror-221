from kafka import KafkaConsumer,KafkaProducer
import json

def health_check(url):
    try:
        # Trying to connecte a Kafka consumer and producer 
        producer = KafkaProducer(bootstrap_servers=url)
        return True,"Kafka is up and running."
    except Exception as e:
        return False,f"Error connecting to Kafka: {e}"
        
        
def connect_to_kafka_producer(url):
    try:
        # connecting to kafka producer and returning same
        producer = KafkaProducer(bootstrap_servers=url,
                                 value_serializer=lambda x: json.dumps(x).encode('utf-8'))
        return True,producer
    except Exception as e:
        return False,f"Error connecting to Kafka Producer: {e}"


def push_event_to_kafka(eventData,topicName,producer):
    try:
        # Sending the event data as a JSON-encoded message
        producer.send(topicName, eventData)
        producer.flush()
        return True,"Event pushed to Kafka successfully."

    except Exception as e:
        return False,f"Error pushing event to Kafka: {e}"



