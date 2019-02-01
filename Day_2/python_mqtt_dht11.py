#!/usr/bin/python
import sys
import Adafruit_DHT
import paho.mqtt.client as mqtt

client = mqtt.Client()
client.connect("iot.eclipse.org", 1883, 60)

while True:
    humidity, temperature = Adafruit_DHT.read_retry(11, 4)
    print 'Temp: {0:0.1f} C  Humidity: {1:0.1f} %'.format(temperature, humidity)
    client.publish('topic/temp', str(temperature))
    client.publish('topic/hum', str(humidity))
client.disconnect()
