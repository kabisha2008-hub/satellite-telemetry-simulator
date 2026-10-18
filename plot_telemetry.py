
import csv
import matplotlib.pyplot as plt

time = []
temperature = []
voltage = []
altitude = []

with open("telemetry.csv", "r") as file:
    reader = csv.DictReader(file)

    for row in reader:
        time.append(int(row["Reading"]))
        temperature.append(float(row["Temperature"]))
        voltage.append(float(row["Voltage"]))
        altitude.append(float(row["Altitude"]))

plt.figure(figsize=(10, 7))

plt.subplot(3, 1, 1)
plt.plot(time, temperature, marker="o")
plt.axhline(40, linestyle="--", label="Temperature limit")
plt.ylabel("Temperature (C)")
plt.legend()
plt.grid(True)

plt.subplot(3, 1, 2)
plt.plot(time, voltage, marker="o")
plt.axhline(3.4, linestyle="--", label="Voltage limit")
plt.ylabel("Voltage (V)")
plt.legend()
plt.grid(True)

plt.subplot(3, 1, 3)
plt.plot(time, altitude, marker="o")
plt.xlabel("Reading number")
plt.ylabel("Altitude (km)")
plt.grid(True)

plt.suptitle("Satellite Telemetry Dashboard")
plt.tight_layout()
plt.show()
