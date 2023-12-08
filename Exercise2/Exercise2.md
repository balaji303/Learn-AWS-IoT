# Exercise 2

## IoT Rules

Gives your devices the ability to interact with other AWS services

It consists of 
    - SQL select statement
    - A topic filter
    - A rule action on
        - Amazon Dynamo DB
        - AWS Lambda
        - Amazon SNS
        - Amazon S3

## What is MQTT?

- MQTT stands for Message Queuing Telemetry Transport.
- It is a machine to machine connectivity protocol,
- That works as a publish and subscribe method. 
- Its a extreme light weight protocol that runs even on small devices
- Using MQTT we can do 
    - Augment or filter a data receieved from a device
    - Write data from a device to a Amazon DynamoDB or any database
    - Save a file to Amazon S3
    - Send a push notification to all users through AWS SNS

## Excerise 2.1

- [x] Create a topic using SNS (Simple Notification Service) 
- [x] Create subscribe for that topic to it via email
- [x] Conform the subscrition email
- [x] Using IAM role add permission for AWS IoT service to publish a notification to that SNS topic
- [x] Create a IoT rule that looks for fuel level using a SQL query
- [x] Start the car and wait for the Email
- [x] Stop the Engine to save the planet

## Device Shadow

- A device shadow is a JSON document, which is used to store and retrieve current state information for a device
- You can use the shadow to get and set the state of the device over MQTT or HTTP
- There are 3 methods

    - Update
    - Get
    - Delete 

## Excersice 2.2

Use Cloud9 environment

Download the new car code

Publish a new state of light on or off

Stop the car engine and change the state

Play with device shadow