
import random
import csv

with open("telemetry.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow([
        "Reading", "Temperature", "Voltage",
        "Altitude", "Status"
    ])

    for t in range(1, 21):
        temperature = round(random.uniform(18, 35), 2)
        voltage = round(random.uniform(3.5, 4.2), 2)
        altitude = round(random.uniform(398, 402), 2)

        # Add one abnormal reading for testing
        if t == 5:
            temperature = 45.0
        if t == 10:
            voltage = 3.2

        if temperature > 40 or voltage < 3.4:
            status = "WARNING"
            print("WARNING at reading", t)
        else:
            status = "NORMAL"

        writer.writerow([
            t, temperature, voltage, altitude, status
        ])

print("Telemetry saved with anomaly detection!")
