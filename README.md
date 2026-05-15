# RADAR-IoT Based Wearable Health Monitoring System

## Overview

This project presents a RADAR-IoT inspired wearable health monitoring prototype using ESP32, biomedical sensors, and Python middleware processing.

The system continuously acquires:
- Raw PPG signals
- Motion/activity data
- Body-contact temperature

The acquired data is processed using threshold-based monitoring and converted into structured health packets for gateway-side monitoring and logging.

---

# System Architecture

```text
Sensors
   ↓
ESP32 Edge Node
   ↓
Serial / BLE Communication
   ↓
Python Middleware Processing
   ↓
Threshold Analysis
   ↓
Structured Health Packets
   ↓
CSV Logging
```

---

# Hardware Components

| Component | Purpose |
|---|---|
| ESP32 DevKit V1 | Edge acquisition controller |
| MAX30102 | Raw PPG signal acquisition |
| MPU6050 | Motion and activity sensing |
| DS18B20 | Body temperature sensing |
| TP4056 | Battery charging module |

---

# Features

- Real-time sensor acquisition
- Multi-sensor integration
- Threshold-based monitoring
- Motion-state classification
- Structured JSON packet generation
- CSV-based continuous logging
- RADAR-IoT inspired workflow

---

# Sensor Parameters

## MAX30102
- IR value
- RED value
- Pulse trend estimation

## MPU6050
- Accelerometer values
- Gyroscope values
- Motion classification

## DS18B20
- Temperature monitoring
- Threshold analysis

---

# Threshold Logic

| Parameter | Status |
|---|---|
| Temperature | LOW / NORMAL / HIGH |
| Motion | Stable / Moderate / High Movement |
| PPG Signal | Weak / Normal Signal |

---

# Software Workflow

## ESP32 Layer
- Sensor interfacing
- Raw data acquisition
- Serial/BLE streaming

## Python Middleware
- Packet parsing
- Threshold analysis
- Motion classification
- JSON packet generation
- CSV logging

---

# Example JSON Packet

```json
{
    "timestamp": "15:42:11",
    "temperature": {
        "value_celsius": 36.8,
        "status": "NORMAL"
    },
    "motion": {
        "motion_status": "STABLE"
    },
    "system_status": "ACTIVE"
}
```

---

# Project Files

## Arduino Files
- i2c_scanner.ino
- mpu6050_raw.ino
- max30102_raw.ino
- ds18b20_test.ino
- combined_sensor_stream.ino
- esp32_ble_server.ino

## Python File
- radar_iot_processing.py

## Generated Logs
- health_monitoring_log.csv

---

# Technologies Used

## Hardware
- ESP32 DevKit V1
- MAX30102
- MPU6050
- DS18B20
- TP4056

## Software
- Arduino IDE
- Python
- Serial Communication
- JSON
- CSV Logging

---

# Current Status

- Multi-sensor prototype developed
- Real-time acquisition pipeline operational
- Threshold-based monitoring implemented
- Structured packet generation completed
- Continuous data logging achieved
- Gateway-oriented architecture validated

---

# Conclusion

The project successfully demonstrates a wearable RADAR-IoT inspired health monitoring workflow using layered acquisition, middleware processing, threshold analysis, and structured data logging.