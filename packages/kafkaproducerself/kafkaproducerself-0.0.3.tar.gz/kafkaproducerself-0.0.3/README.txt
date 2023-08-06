It provides general functions to get kafka producer and publish events using it, additonally a health check also there to make sure connections is live.

It provides three functions :

-- health_check  
accepts url as parameter
returns tuple
True/False : Depending if connection is on or not
String : Success or failure message


-- connect_to_kafka_producer 
accepts url as parameter
returns tuple
True/False : Depending on producer status
Obj/String : producer object if connected else error message


-- push_event_to_kafka
accepts eventData, topicName, producer as parameters
returns tuple
True/False : Depending if message published or not
String : Success or failure message