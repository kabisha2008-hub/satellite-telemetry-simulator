
import streamlit as st
import pandas as pd

st.set_page_config(page_title="Satellite Dashboard", layout="wide")

st.title("🛰️ Satellite Telemetry Dashboard")
st.caption("Simulated satellite data monitoring system")

try:
    df = pd.read_csv("telemetry.csv")

    # Basic data summary
    total = len(df)
    warnings = (df["Status"] == "WARNING").sum()

    c1, c2, c3 = st.columns(3)
    c1.metric("Total Readings", total)
    c2.metric("Warnings", int(warnings))
    c3.metric("Average Temperature",
              f"{df['Temperature'].mean():.2f} °C")

    st.subheader("Temperature")
    st.line_chart(df.set_index("Reading")["Temperature"])

    st.subheader("Battery Voltage")
    st.line_chart(df.set_index("Reading")["Voltage"])

    st.subheader("Altitude")
    st.line_chart(df.set_index("Reading")["Altitude"])

    st.subheader("Telemetry Data")
    st.dataframe(df, use_container_width=True)

    st.subheader("Anomaly Readings")
    alerts = df[df["Status"] == "WARNING"]

    if alerts.empty:
        st.success("No anomalies detected!")
    else:
        st.warning(f"{len(alerts)} unusual reading(s) detected.")
        st.dataframe(alerts, use_container_width=True)
        
        st.download_button(
        label="Download Telemetry CSV",
        data=df.to_csv(index=False),
        file_name="satellite_telemetry_report.csv",
        mime="text/csv"
        )

except FileNotFoundError:
    st.error("telemetry.csv not found.")
    st.info("First run: python satellite_telemetry.py")

except KeyError as e:
    st.error(f"CSV column missing: {e}")
    st.info("Run satellite_telemetry.py again to create the correct CSV.")
