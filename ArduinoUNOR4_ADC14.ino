void setup(){
  analogReadResolution(14); //change to 14-bit resolution
  Serial.begin(2000000);
}

void loop(){
  int reading = analogRead(A0); // returns a value between 0-16383
  Serial.println(reading);
  delayMicroseconds(10); // sleep 10 microseconds
}