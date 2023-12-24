# Exercise 3

## X.509 Certificate

1. This certificate is used to know the endPoints

1. Used in many internet service protocols

    1. TSL
    1. SSL
    1. HTTPS

1. In a browser, although it could be possible to store the certificate and private key of your Car Thing in your JavaScript code, that wouldn't be very secure. Also, using MQTT in a browser isn't straight forward. As it's a browser, the favorite protocol is HTTPS for communication outbound. Although it is supported by the AWS IoT service, it has been proven that the HTTPS protocol doesn't have the same performance as the MQTT protocol when many messages are sent. That is due to the overhead of HTTPS as the connection needs to be re-established for every messages. As opposed to MQTT where one connection can be used for all messages to be sent. Unfortunately, using MQTT directly in the browser isn't an option. Instead, MQTT over a WebSocket is a lot easier to do. Although, there is an overhead of connection establishment with a WebSocket, we will gain back on the benefit of the small overhead of MQTT inside the WebSocket.