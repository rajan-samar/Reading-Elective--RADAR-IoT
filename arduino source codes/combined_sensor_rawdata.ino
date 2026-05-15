#include <Wire.h>

#include <Adafruit_MPU6050.h>
#include <Adafruit_Sensor.h>

#include "MAX30105.h"

#include <OneWire.h>
#include <DallasTemperature.h>

// ---------------- MPU6050 ----------------

Adafruit_MPU6050 mpu;

// ---------------- MAX30102 ----------------

MAX30105 particleSensor;

// ---------------- DS18B20 ----------------

#define ONE_WIRE_BUS 4

OneWire oneWire(ONE_WIRE_BUS);

DallasTemperature tempSensor(&oneWire);

// ------------------------------------------------

void setup() {

  Serial.begin(115200);

  Wire.begin(21,22);

  // MPU6050 Initialization
  if (!mpu.begin()) {

    Serial.println("MPU6050 NOT Found");

    while (1);
  }

  // MAX30102 Initialization
  if (!particleSensor.begin(Wire, I2C_SPEED_STANDARD)) {

    Serial.println("MAX30102 NOT Found");

    while (1);
  }

  particleSensor.setup();

  particleSensor.setPulseAmplitudeRed(0x1F);
  particleSensor.setPulseAmplitudeIR(0x1F);

  // DS18B20 Initialization
  tempSensor.begin();

  Serial.println("All Sensors Initialized");
}

// ------------------------------------------------

void loop() {

  // MPU6050 Data
  sensors_event_t a, g, temp;

  mpu.getEvent(&a, &g, &temp);

  // MAX30102 Data
  long irValue = particleSensor.getIR();

  long redValue = particleSensor.getRed();

  // DS18B20 Data
  tempSensor.requestTemperatures();

  float bodyTemp = tempSensor.getTempCByIndex(0);

  // ------------------------------------------------
  // Combined Raw Stream
  // ------------------------------------------------

  Serial.print("IR:");
  Serial.print(irValue);

  Serial.print(",");

  Serial.print("RED:");
  Serial.print(redValue);

  Serial.print(",");

  Serial.print("TEMP:");
  Serial.print(bodyTemp);

  Serial.print(",");

  Serial.print("AX:");
  Serial.print(a.acceleration.x);

  Serial.print(",");

  Serial.print("AY:");
  Serial.print(a.acceleration.y);

  Serial.print(",");

  Serial.print("AZ:");
  Serial.print(a.acceleration.z);

  Serial.print(",");

  Serial.print("GX:");
  Serial.print(g.gyro.x);

  Serial.print(",");

  Serial.print("GY:");
  Serial.print(g.gyro.y);

  Serial.print(",");

  Serial.print("GZ:");
  Serial.println(g.gyro.z);

  delay(1000);
}