## IOT class
This repository contains code for IOT class, `Day 1` has codes on NodeMCU for PIR and DHT11 sensor along with Paho MQTT 
 

## Dependencies required 
  1. `Paho MQTT Client` : https://www.eclipse.org/paho/clients/python/docs/
  2. `SKlearn ML framework` : https://scikit-learn.org/stable/
  3. `TensorFlow` : https://www.tensorflow.org/install

## Day 1 essentials:

## Adding NodeMCU support to Arduino IDE
Here's how to program the NodeMCU using the Arduino IDE.

`Step 1: Connect your NodeMCU to your computer`
You need a USB micro B cable to connect with the board. Once you are plugged in, a `blue LED` will start flashing. If your computer is not able to detect the NodeMCU board, you may need to download the driver from this `link` https://www.silabs.com/products/development-tools/software/usb-to-uart-bridge-vcp-drivers.

`Step 2: Open Arduino IDE`
You need to have at least Arduino IDE version 1.6.4 to proceed with this.

Go to File > Preferences. In the "Additional Boards Manager URLs" field, type (or copy-paste) http://arduino.esp8266.com/stable/package_esp8266com_index.json. Don't forget to click OK!

<img src="https://github.com/debjyotiC/IOT_class/blob/master/images/node-mcu-arduino-1.jpg" width="580">

Then go to  Tools > Board > Board Manager. Type "esp8266" in the search field. The entry "esp8266 by ESP8266 Community" should appear. Click that entry and look for the install button on the lower right.

<img src="https://github.com/debjyotiC/IOT_class/blob/master/images/node-mcu-arduino-2.jpg" width="580">

Once the download is complete, you can start coding!

`Step 3: Make a LED blink using NodeMCU`

For our first program, we'll blink a LED connected to one of the digital pins of the board. But before that, you need to know that the pin names printed on the board are not the pin names we'll be using for our program. BTW, I'm using NodeMCU V1.0. See my NodeMCU pinout article if you have the other versions of the board.

<img src="https://github.com/debjyotiC/IOT_class/blob/master/images/NodeMCUv1.0-pinout.jpg" width="580">

In this example, I'll connect the LED to D7 as it is printed on the board. D7 is GPIO13 according to the image above. And so here's my code (which is basically the example Blink code in Arduino):

```
// the setup function runs once when you press reset or power the board
void setup() {
  // initialize digital pin 13 as an output.
  pinMode(13, OUTPUT);
}
 
// the loop function runs over and over again forever
void loop() {
  digitalWrite(13, HIGH);   // turn the LED on (HIGH is the voltage level)
  delay(1000);              // wait for a second
  digitalWrite(13, LOW);    // turn the LED off by making the voltage LOW
  delay(1000);              // wait for a second
}
```

## Day 2 essentials:

We’ll be using the Adafruit DHT11 Python library. You can download the library using Git, so if you don’t have Git installed on your Pi already, enter this at the command prompt:

`sudo apt-get install git-core`

Note: If you get an error installing Git, run sudo apt-get update and try it again.

To install the Adafruit DHT11 library:

1. Enter this at the command prompt to download the library:

`git clone https://github.com/adafruit/Adafruit_Python_DHT.git`

2. Change directories with:

`cd Adafruit_Python_DHT`

3. Now enter this:

`sudo apt-get install build-essential python-dev`

4. Then install the library with:

`sudo python setup.py install`

Test code for DHT 11 on the Raspberry Pi

```
#!/usr/bin/python
import sys
import Adafruit_DHT

while True:

    humidity, temperature = Adafruit_DHT.read_retry(11, 4)

    print 'Temp: {0:0.1f} C  Humidity: {1:0.1f} %'.format(temperature, humidity)
```
Wiring schema

<img src="https://github.com/debjyotiC/IOT_class/blob/master/images/How-to-Setup-the-DHT11-on-the-Raspberry-Pi-Three-pin-DHT11-Wiring-Diagram-768x359.png" width="580">

The wiring scheme for LED on the RPi

<img src="https://github.com/debjyotiC/IOT_class/blob/master/images/01_Blinking-LED_bb-768x583.jpg" width="580">


# Links
1. Link to download `PyCharm` : https://www.jetbrains.com/pycharm/download/#section=windows
2. Link to download `Anaconda` : https://www.anaconda.com/distribution/
3. Link to download `GitHub Desktop` : https://desktop.github.com/
