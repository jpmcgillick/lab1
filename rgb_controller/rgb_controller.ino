// define pins
#define ledR 3
#define ledG 5
#define ledB 6

void setup(){
  Serial.begin(9600)
}
// the loop routine runs over and over again forever:

void loop() {
  int val = analogRead(A0);
  // turn the LED on (HIGH is the voltage level)
  ///analogWrite(ledR, 255);
  analogWrite(ledG, val/4);
  Serial.print(val);
}
