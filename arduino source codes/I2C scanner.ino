#include <Wire.h>

void setup() {

  Wire.begin(21,22);

  Serial.begin(115200);

  Serial.println("\nI2C Scanner Started");
}

void loop() {

  byte error, address;
  int devices = 0;

  Serial.println("\nScanning...");

  for(address = 1; address < 127; address++) {

    Wire.beginTransmission(address);

    error = Wire.endTransmission();

    if(error == 0) {

      Serial.print("I2C Device Found at 0x");

      if(address < 16)
        Serial.print("0");

      Serial.println(address, HEX);

      devices++;
    }
  }

  if(devices == 0) {

    Serial.println("No I2C Devices Found");
  }

  Serial.println("----------------------");

  delay(3000);
}