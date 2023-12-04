# Learn-AWS-IoT
💡 Learn how to use Amazon Web Services Internet of Things (IoT) service to build connected applications.

## Device GateWay

1. This is the first portion of IoT core
1. Low latency and low overhead communications
<!-- Todo deviceGateway image here -->

## Message Broker

1. High throughput PUB-SUB message broker
1. Securely transfers message To and From IoT devices
<!-- Todo image here -->

## Device Shadow

1. This enabled cloud and mobile devices to set and get data using simple REST APIs

## Registry

1. This maintains the identity for devices and tracks the metadata such as attributes and capabilities
1. *Assigns unique Identity* to each devices
1. This is the first step in setting up device
1. *Register a Thing* is the first step in that feature that registers it.
1. Followed by adding *Certificate* which is a x509 and a Private Key, Make sure to secure it :)
1. Associate with the device
1. Activate the device
1. Almost there now *Policy* for our thing
1. Create a Policy, Give * and attach the policy to the device
1. [Video Tutorial](https://www.youtube.com/watch?v=0vbk8A58Qd8)

## What we do

1. Create cars as edge devices
1. Make it send telemetry data to AWS IoT Core
1. Shadow those cars
1. Create Cognito identites
1. AWS S3 based static website to control the cars
1. Add GreenGrass core subscription to the edge devices
1. Add AWS Lambda to the edge devices
<!-- Todo WhatWeDo image here -->