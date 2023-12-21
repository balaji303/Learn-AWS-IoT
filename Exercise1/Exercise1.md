# Exercise 1

1. Create a Cloud9 IDE Environment which we use like SandBox
1. Create Things from AWS IoT Core
    
    1. Create an IoT Thing
    1. Create Certificate for MQTT authentication
    1. Create a Policy
    1. Combine Thing,certificate and Policy
    1. Create another Things using CLI

1. Once Car is ignited, Download a Node.js code to PC and run it

1. Test the cars using MQTT test client by subscribing it to a topic

1. Dont forget to stop the car to save the planet

[Exercise 1](https://aws-tc-largeobjects.s3.amazonaws.com/OTP-AWS_D5-2019/v1.0/instructions/Exercise1.1.html)
https://docs.aws.amazon.com/iot/latest/developerguide/iot-moisture-policy.html

## Detailed Step by step

1. Go to AWS IoT -> Security -> Policies
1. Create Policy and paste the JSON content

- [x] IAM_Policy created Successfully
- [x] Created a IAM user
- [x] Attach the IAM_Policy to the IAM_User
- [x] Create a Cloud9 environment
- [x] Setup your Cloud9 Environment
- [x] download i.e, wget the Car code (node.js)
- [x] download i.e, wget the AWS IoT CA Public Cert (from link)
- [x] Create a IoT thing
- [x] Create Certificate
- [x] Create Policy for thing
- [x] Attach certificate and policy
- [x] Upload your Certificate and Private Key to Cloud9
- [x] Create a IoT thing using CLI
- [x] Create Certificate using CLI
- [x] Create Policy for thing using CLI
- [x] Attach certificate and policy using CLI
- [x] Get the endpoint.json file
- [x] Engine ON for car1
- [x] Engine ON for car2
- [x] Subscribe to a MQTT topic
- [x] Check the Logs
Link: https://010703111265.signin.aws.amazon.com/console


## Summary

- Device Gateway => An AWS IoT Core feature enables communication between publishers and subscribers, scales automatically, and supports the MQTT, WebSockets, and HTTP 1.1 protocols

- Registry => An AWS IoT Core feature establishes an identity for devices and tracks metadata such as the devices’ attributes and capabilities

aws iot attach-policy --policy-name CarPolicy --target certificateArn_changeme
arn:aws:iot:us-east-1:010703111265:cert/d257c7c7e5beb8b0aec4b12ab71011fe6594afd3c5da0e3d462517c0ddb3ad57


aws iot attach-policy --policy-name CarPolicy --target arn:aws:iot:us-east-1:010703111265:cert/d257c7c7e5beb8b0aec4b12ab71011fe6594afd3c5da0e3d462517c0ddb3ad57

aws iot attach-thing-principal --thing-name car2 --principal certificateArn_changeme
arn:aws:iot:us-east-1:010703111265:cert/d257c7c7e5beb8b0aec4b12ab71011fe6594afd3c5da0e3d462517c0ddb3ad57

aws iot attach-thing-principal --thing-name car2 --principal arn:aws:iot:us-east-1:010703111265:cert/d257c7c7e5beb8b0aec4b12ab71011fe6594afd3c5da0e3d462517c0ddb3ad57