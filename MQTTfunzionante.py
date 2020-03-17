import paho.mqtt.client as mqtt
import time

def on_connect(client, userdata, flags, rc):
    print("connected with code "+ str(rc))
    # substrice topic
    client.subscribe("Topic/#")

def on_message(client, userdata, msg):
    print(str(msg.payload))


client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.username_pw_set("fkjqkoul","wK0aUWpQWS35")
client.connect("tailor.cloudmqtt.com", 16434 , 60 )

client.loop_forever()

time.sleep(1)
while True:
    client.publish("Tutorial2", "Getting started with MQTT TEST")
    time.sleep(15)

client.loop_stop()
client.disconnect()



