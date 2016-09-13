#!/usr/bin/env/ python

import paho.mqtt.client as mqtt

# The callback for when the client connects to the broker.
def on_connect(client, userdata, rc)
    client.subscribe("lumo/button")

# The callback for when a PUBLISH message is received from the broker
def on_message(client, userdata, msg)
    topic=msg.topic


