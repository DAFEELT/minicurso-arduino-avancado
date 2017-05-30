#include<SoftwareSerial.h>

SoftwareSerial BTSerial(10,11); //TX, RX


void setup() {
    Serial.begin(9600);
    BTSerial.begin(9600);
    Serial.print("Arduino Iniciado...");
}

void loop() {
    //Se tiver algo indo do monitor serial enviar para o bluetooth
    if(Serial.available()){
        BTSerial.write(Serial.read());
    }
    //Se tiver algo indo do bluetooth enviar para o monitor serial
    if(BTSerial.available()){
        Serial.write(BTSerial.read());
    }
}
