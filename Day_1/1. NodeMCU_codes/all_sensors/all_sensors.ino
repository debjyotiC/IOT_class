#include <ESP8266WiFi.h>;
#include <WiFiClient.h>;
#include <ThingSpeak.h>;
#include <DHT.h>

const char* ssid = ""; //Your Network SSID
const char* password = ""; //Your Network Password

int val;
int LDRpin = A0; //LDR Pin Connected at A0 Pin
#define DHTPIN 0          //pin where the dht11 is connected
DHT dht(DHTPIN, DHT11);
WiFiClient client;

unsigned long myChannelNumber = ; //Your Channel Number (Without Brackets)
const char * myWriteAPIKey = ""; //Your Write API Key

void setup(){
Serial.begin(9600);
WiFi.begin(ssid, password);
dht.begin();
ThingSpeak.begin(client);
}
void loop(){
val = analogRead(LDRpin); //Read Analog values and Store in val variable
Serial.print(val); //Print on Serial Monitor
float h = dht.readHumidity();
float t = dht.readTemperature();
if (isnan(h) || isnan(t)){
   Serial.println("Failed to read from DHT sensor!");
   return;
}

ThingSpeak.setField(1, t);
ThingSpeak.setField(2, h);
ThingSpeak.setField(3, val);
ThingSpeak.writeFields(myChannelNumber, myWriteAPIKey);

//ThingSpeak.writeField(myChannelNumber, 1,t, myWriteAPIKey); //Update in ThingSpeak
//ThingSpeak.writeField(myChannelNumber, 2,h, myWriteAPIKey); //Update in ThingSpeak
//ThingSpeak.writeField(myChannelNumber, 3,val, myWriteAPIKey); //Update in ThingSpeak
delay(15000);
}
