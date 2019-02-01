int sensor = 0;  // Digital pin D7

void setup() {
  Serial.begin(9600);
  pinMode(sensor, INPUT);   // declare sensor as input
  pinMode(LED_BUILTIN, OUTPUT);  // declare LED as output
}
void loop() {

  long state = digitalRead(sensor);
    if(state == HIGH) {
      digitalWrite (LED_BUILTIN, HIGH);
      Serial.println("Motion detected!");
      delay(1000);
    }
    else {
      digitalWrite (LED_BUILTIN, LOW);
      Serial.println("Motion absent!");
      delay(1000);
      }
}
