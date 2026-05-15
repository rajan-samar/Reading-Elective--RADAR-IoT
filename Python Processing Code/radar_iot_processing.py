import serial
import time
import math
import json
import csv
import os

from datetime import datetime

# =========================================================
# RADAR-IoT HEALTH MONITORING SYSTEM
# =========================================================

# ---------------------------------------------------------
# SERIAL PORT CONFIGURATION
# ---------------------------------------------------------

try:

    ser = serial.Serial('COM5', 115200)

    time.sleep(2)

    print("\nESP32 Connected Successfully\n")

except:

    print("\nESP32 Connection Failed\n")

    exit()

# =========================================================
# SYSTEM HEADER
# =========================================================

print("====================================================")
print("      RADAR-IoT HEALTH MONITORING SYSTEM")
print("====================================================")

# =========================================================
# THRESHOLDS
# =========================================================

# Temperature Thresholds
TEMP_LOW = 35.0
TEMP_HIGH = 37.5

# Motion Thresholds
MOTION_MODERATE = 11
MOTION_HIGH = 15

# PPG Signal Threshold
IR_LOW = 50000

# =========================================================
# CSV FILE SETUP
# =========================================================

csv_file = "health_monitoring_log.csv"

file_exists = os.path.isfile(csv_file)

with open(csv_file, mode='a', newline='') as file:

    writer = csv.writer(file)

    if not file_exists:

        writer.writerow([
            "Timestamp",

            "IR_Value",
            "RED_Value",

            "Temperature",
            "Temperature_Status",

            "Motion_Magnitude",
            "Motion_Status",

            "Pulse_Status",

            "AX",
            "AY",
            "AZ",

            "GX",
            "GY",
            "GZ"
        ])

# =========================================================
# MAIN LOOP
# =========================================================

while True:

    try:

        # -------------------------------------------------
        # READ SERIAL DATA
        # -------------------------------------------------

        line = ser.readline().decode('utf-8').strip()

        # Ignore Empty Packets
        if not line:
            continue

        # -------------------------------------------------
        # SHOW RAW PACKET
        # -------------------------------------------------

        print("\nRaw Packet:")
        print(line)

        # -------------------------------------------------
        # PARSE SENSOR DATA
        # -------------------------------------------------

        data = {}

        values = line.split(",")

        for item in values:

            if ":" in item:

                key, value = item.split(":")

                data[key] = float(value)

        # -------------------------------------------------
        # EXTRACT SENSOR VALUES
        # -------------------------------------------------

        ir = data["IR"]
        red = data["RED"]

        temp = data["TEMP"]

        ax = data["AX"]
        ay = data["AY"]
        az = data["AZ"]

        gx = data["GX"]
        gy = data["GY"]
        gz = data["GZ"]

        # =================================================
        # TEMPERATURE ANALYSIS
        # =================================================

        if temp < TEMP_LOW:

            temp_status = "LOW"

        elif temp > TEMP_HIGH:

            temp_status = "HIGH"

        else:

            temp_status = "NORMAL"

        # =================================================
        # MOTION ANALYSIS
        # =================================================

        motion_magnitude = math.sqrt(
            ax**2 +
            ay**2 +
            az**2
        )

        if motion_magnitude < MOTION_MODERATE:

            motion_status = "STABLE"

        elif motion_magnitude < MOTION_HIGH:

            motion_status = "MODERATE MOVEMENT"

        else:

            motion_status = "HIGH MOVEMENT"

        # =================================================
        # PPG SIGNAL ANALYSIS
        # =================================================

        if ir < IR_LOW:

            pulse_status = "WEAK SIGNAL"

        else:

            pulse_status = "NORMAL SIGNAL"

        # =================================================
        # TIMESTAMP
        # =================================================

        timestamp = datetime.now().strftime("%H:%M:%S")

        # =================================================
        # RADAR-IoT STYLE STRUCTURED PACKET
        # =================================================

        radar_packet = {

            "timestamp": timestamp,

            "ppg_signal": {

                "ir_value": ir,
                "red_value": red,
                "signal_status": pulse_status
            },

            "temperature": {

                "value_celsius": round(temp, 2),
                "status": temp_status
            },

            "motion": {

                "accelerometer": {

                    "ax": ax,
                    "ay": ay,
                    "az": az
                },

                "gyroscope": {

                    "gx": gx,
                    "gy": gy,
                    "gz": gz
                },

                "motion_magnitude": round(
                    motion_magnitude,
                    2
                ),

                "motion_status": motion_status
            },

            "system_status": "ACTIVE"
        }

        # =================================================
        # FORMATTED OUTPUT
        # =================================================

        print("\n================================================")

        print(f"Timestamp         : {timestamp}")

        print("================================================")

        print(f"\nIR Value          : {ir}")
        print(f"RED Value         : {red}")

        print(f"\nTemperature       : {temp:.2f} °C")

        print(f"Temperature Status: {temp_status}")

        print("\nAccelerometer")

        print(f"AX                : {ax}")
        print(f"AY                : {ay}")
        print(f"AZ                : {az}")

        print("\nGyroscope")

        print(f"GX                : {gx}")
        print(f"GY                : {gy}")
        print(f"GZ                : {gz}")

        print(f"\nMotion Magnitude  : {motion_magnitude:.2f}")

        print(f"Motion Status     : {motion_status}")

        print(f"\nPulse Status      : {pulse_status}")

        print("\nRADAR-IoT Status  : ACTIVE")

        # =================================================
        # PRINT JSON PACKET
        # =================================================

        print("\nRADAR-IoT Structured Packet:\n")

        print(
            json.dumps(
                radar_packet,
                indent=4
            )
        )

        # =================================================
        # CSV LOGGING
        # =================================================

        with open(csv_file, mode='a', newline='') as file:

            writer = csv.writer(file)

            writer.writerow([

                timestamp,

                ir,
                red,

                round(temp, 2),
                temp_status,

                round(motion_magnitude, 2),
                motion_status,

                pulse_status,

                ax,
                ay,
                az,

                gx,
                gy,
                gz
            ])

        print("\nData Logged Successfully")

        print("\n------------------------------------------------")

    except Exception as e:

        print("\nParsing Error:", e)