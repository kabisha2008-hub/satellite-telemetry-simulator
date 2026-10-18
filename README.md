
# 🛰️ Satellite Telemetry Simulator and Anomaly Detection Dashboard

## 📌 About the Project
This project simulates satellite telemetry data using Python.
It monitors temperature, battery voltage, and altitude,
detects unusual readings, and displays the results through
an interactive Streamlit dashboard.

## ✨ Features
- Generates 20 simulated satellite readings
- Monitors temperature, voltage, and altitude
- Detects abnormal temperature and voltage readings
- Saves telemetry data in a CSV file
- Displays graphs and summary metrics
- Shows warning readings in a dashboard
- Downloads telemetry reports as CSV

## 🛠️ Technologies Used
- Python
- Pandas
- Matplotlib
- Streamlit
- CSV

## 📂 Project Structure

```text
satellite-telemetry-simulator/
├── satellite_telemetry.py
├── plot_telemetry.py
├── app.py
├── telemetry.csv
└── README.md
```

## ⚙️ Installation

Install the required libraries:

```bash
python -m pip install streamlit pandas matplotlib
```

## ▶️ How to Run

### Step 1: Generate Satellite Data

```bash
python satellite_telemetry.py
```

### Step 2: Run the Graph Plotter (Optional)

```bash
python plot_telemetry.py
```

### Step 3: Launch the Dashboard

```bash
python -m streamlit run app.py
```

The dashboard will open in your browser.

## 📊 Anomaly Detection
The system displays a warning when:
- Temperature is above 40°C
- Battery voltage is below 3.4 V

These thresholds are used for demonstration only.

## 🎯 Objective
To learn how satellite-inspired telemetry data can be
generated, analysed, visualised, and monitored using Python.

## 🔮 Future Improvements
- Use real public satellite datasets
- Add more sensor parameters
- Improve anomaly detection
- Add interactive data filters

## ⚠️ Disclaimer
This is an educational simulation project.
It does not connect to a real satellite, and its data
and thresholds are not actual spacecraft measurements.
