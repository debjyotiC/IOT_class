import paho.mqtt.client as mqtt

client = mqtt.Client()
client.connect("mqtt.eclipseprojects.io", 1883, 60)

client.publish('topic/test', 'hi')


client.disconnect()