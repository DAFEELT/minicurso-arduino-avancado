#include <SoftwareSerial.h>
SoftwareSerial BTSerial(10, 11); // RX | TX

void setup() {
  Serial.begin(9600);
  BTSerial.begin(9600);
  delay(200);
}

void loop() {
  // Keep reading from HC-05 and send to Arduino Serial Monitor
  if (BTSerial.available()) {
    Serial.write(BTSerial.read());
  }

  // Keep reading from Arduino Serial Monitor and send to BT Module
  if (Serial.available()) {
    BTSerial.write(Serial.read());
  }

}
