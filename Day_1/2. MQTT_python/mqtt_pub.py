import paho.mqtt.client as mqtt

chat = raw_input("Chat:")

client = mqtt.Client()
client.connect("iot.eclipse.org", 1883, 60)
client.publish('topic/test', chat)
client.disconnect()
