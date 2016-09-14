#!/usr/bin/env/ python

import paho.mqtt.client as mqtt

# The callback for when the client connects to the broker.
def on_connect(client, userdata, rc)
    client.subscribe("lumo/button")

# The callback for when a PUBLISH message is received from the broker
def on_message(client, userdata, msg)
    topic=msg.topic
    data = msg.payload

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect("localhost", 1883, 60)

#Blocking call that handles all network traffic and dispatches callbacks.
#Also handles reconnection
client.loop_forever()

