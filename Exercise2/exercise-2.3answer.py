# Chat application between cars

'''
* Copyright 2010-2019 Amazon.com, Inc. or its affiliates. All Rights Reserved.
*
* Licensed under the Apache License, Version 2.0 (the "License").
* You may not use this file except in compliance with the License.
* A copy of the License is located at
*
*  http://aws.amazon.com/apache2.0
*
* or in the "license" file accompanying this file. This file is distributed
* on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either
* express or implied. See the License for the specific language governing
* permissions and limitations under the License.
'''
import AWSIoTPythonSDK
# Import the AWS IoT Device SDK
from AWSIoTPythonSDK.MQTTLib import AWSIoTMQTTClient

# Import json for parson endpoint.json file
import json

# Import os for finding name of current directory
import os

# Load the endpoint from file
with open('/home/ec2-user/environment/endpoint.json') as json_file:  
    data = json.load(json_file)

# Fetch the deviceName from the current folder name
deviceName = os.path.split(os.getcwd())[1]

# Set the destinationDeviceName depending on this deviceName
if deviceName == 'car1':
    destinationDeviceName = 'car2'
    print('deviceName:'+deviceName+' destinationDeviceName:'+destinationDeviceName)
else:
    destinationDeviceName = 'car1'

# Build useful variable for code
subTopic = '@Balaji303/' + deviceName
pubTopic = '@Balaji303/' + destinationDeviceName
keyPath = 'private.pem.key'
certPath = 'certificate.pem.crt'
caPath = '/home/ec2-user/environment/root-CA.crt'
clientId = deviceName
host = data['endpointAddress']
port = 8883


# 1: Use the AWSIoTMQTTClient library to create your AWSIoTMQTTClient 
#         client using the useful variable above and connect it to AWS IoT
# Creating instance of the call 
balajiAWSIoTMQTTClient = AWSIoTMQTTClient(clientId)
# Configuring the endpoint with port
balajiAWSIoTMQTTClient.configureEndpoint(host,port)
# Configuring the credentials
balajiAWSIoTMQTTClient.configureCredentials(caPath,keyPath,certPath)
#Now connect the device
balajiAWSIoTMQTTClient.connect()

# 2: Create a function that will be called when a new message is received 
#         and output its content in the console.
def callBackFunction(client, userdata, message):
     print("----- START of Payload -----")
     print("Received a new message: ")
     print(message.payload.decode())
     print("This message is from the topic:")
     print(message.topic)
     print("----- END of Payload -----\n\n")


# 3: Subscribe to the subTopic IoT Topic and use the function created in
#         TODO 2 as the callback
balajiAWSIoTMQTTClient.subscribe(subTopic,1,callBackFunction)


# Function to publish payload to IoT topic
def publishToIoTTopic(topic, payload):
    # 4: Implement function to publish to specified IoT topic using device object
    #         that you will create
    balajiAWSIoTMQTTClient.publish(topic, payload,1)    
    


#################################
# DON'T EDIT ANYTHING PAST THIS #
#################################
# Infinite loop reading console input and publishing what it finds
while True:
    message = input('Enter a message on the next line to send to ' + pubTopic + ':\r\n')
    
    # Calling function to publish to IoT Topic
    publishToIoTTopic(pubTopic, message)