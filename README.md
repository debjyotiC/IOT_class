## IOT class
This repository contains code for IOT class the repository, `Day 1` has codes on NodeMCU for PIR and DHT11 sensor along with Paho MQTT 
 

## Dependencies required 
  1. `Paho MQTT Client` : https://www.eclipse.org/paho/clients/python/docs/
  2. `SKlearn ML framework` : https://scikit-learn.org/stable/
  3. `TensorFlow` : 

## Adding NodeMCU support to Arduino IDE
Here's how to program the NodeMCU using the Arduino IDE.

`Step 1:` Connect your NodeMCU to your computer
You need a USB micro B cable to connect the board. Once you plugged it in, a blue LED will start flashing. If your computer is not able to detect the NodeMCU board, you may need to download the driver on this page.

`Step 2:` Open Arduino IDE
You need to have at least Arduino IDE version 1.6.4 to proceed with this.

Go to File > Preferences. In the "Additional Boards Manager URLs" field, type (or copy-paste) http://arduino.esp8266.com/stable/package_esp8266com_index.json. Don't forget to click OK!

<img src="https://github.com/debjyotiC/IOT_class/blob/master/images/node-mcu-arduino-1.jpg" width="580">

Then go to  Tools > Board > Board Manager. Type "esp8266" in the search field. The entry "esp8266 by ESP8266 Community" should appear. Click that entry and look for the install button on the lower right.

<img src="https://github.com/debjyotiC/IOT_class/blob/master/images/node-mcu-arduino-2.jpg" width="580">

Once the download is complete, you can start coding!

`Step 3:` Make a LED blink using NodeMCU
For our first program, we'll blink a LED connected to one of the digital pins of the board. But before that, you need to know that the pin names printed on the board are not the pin names we'll be using for our program. BTW, I'm using NodeMCU V1.0. See my NodeMCU pinout article if you have the other versions of the board.
<img src="https://github.com/debjyotiC/IOT_class/blob/master/images/NodeMCUv1.0-pinout.jpg" width="580">

In this example, I'll connect the LED to D7 as it is printed on the board. D7 is GPIO13 according to the image above. And so here's my code (which is basically the example Blink code in Arduino):

<img src="https://github.com/debjyotiC/IOT_class/blob/master/images/giphy.gif" width="580">


# Links
Link to download `PyCharm` : https://www.jetbrains.com/pycharm/download/#section=windows

Link to download `Anaconda` : https://www.anaconda.com/distribution/
