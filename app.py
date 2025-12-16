import streamlit as st
import joblib
import numpy as np

# Load trained model
model = joblib.load('models/soc_model.pkl')

st.title("EV Battery SOC Predictor 🔋")

voltage = st.number_input("Voltage (V)", min_value=0.0)
current = st.number_input("Current (A)", min_value=0.0)
temperature = st.number_input("Temperature (°C)")

if st.button("Predict SOC"):
    soc = model.predict([[voltage, current, temperature]])
    st.success(f"Predicted SOC: {soc[0]:.2f}%")
