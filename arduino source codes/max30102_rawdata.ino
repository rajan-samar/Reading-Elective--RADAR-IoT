#include <Wire.h>
#include "MAX30105.h"

MAX30105 particleSensor;

void setup() {

  Serial.begin(115200);

  Wire.begin(21,22);

  if (!particleSensor.begin(Wire, I2C_SPEED_STANDARD)) {

    Serial.println("MAX30102 NOT Found");

    while (1);
  }

  Serial.println("MAX30102 Ready");

  particleSensor.setup();

  particleSensor.setPulseAmplitudeRed(0x1F);
  particleSensor.setPulseAmplitudeIR(0x1F);
}

void loop() {

  long irValue = particleSensor.getIR();

  long redValue = particleSensor.getRed();

  Serial.print("IR:");

  Serial.print(irValue);

  Serial.print(",");

  Serial.print("RED:");

  Serial.println(redValue);

  delay(1000);
}