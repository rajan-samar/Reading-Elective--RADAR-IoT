#include <Wire.h>
#include <Adafruit_MPU6050.h>
#include <Adafruit_Sensor.h>

Adafruit_MPU6050 mpu;

void setup() {

  Serial.begin(115200);

  Wire.begin(21,22);

  if (!mpu.begin()) {

    Serial.println("MPU6050 NOT Found");

    while (1);
  }

  Serial.println("MPU6050 Ready");
}

void loop() {

  sensors_event_t a, g, temp;

  mpu.getEvent(&a, &g, &temp);

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