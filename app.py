import streamlit as st
import joblib
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# -----------------------------
# Page Configuration
# -----------------------------
st.set_page_config(
    page_title="EV Battery SOC Predictor",
    page_icon="🔋",
    layout="wide"
)

# -----------------------------
# Load Model & Data
# -----------------------------
model = joblib.load('models/soc_model.pkl')

# Load NASA cleaned data for visualization
data = pd.read_csv('data/nasa/clean_nasa_soc_data.csv')

# -----------------------------
# Sidebar
# -----------------------------
st.sidebar.title("🔧 Input Parameters")
st.sidebar.markdown("Enter battery parameters:")

voltage = st.sidebar.number_input("Voltage (V)", min_value=0.0, value=3.7)
current = st.sidebar.number_input("Current (A)", min_value=0.0, value=1.5)
temperature = st.sidebar.number_input("Temperature (°C)", value=25.0)

predict_btn = st.sidebar.button("🔮 Predict SOC")

show_plots = st.sidebar.checkbox("📊 Show Visualizations")

# -----------------------------
# Main Title
# -----------------------------
st.title("🔋 EV Battery State of Charge (SOC) Predictor")
st.markdown(
    """
This application predicts the **State of Charge (SOC)** of an Electric Vehicle battery  
using a **Machine Learning model trained on NASA Lithium-Ion Battery data**.
"""
)

# -----------------------------
# Prediction Section
# -----------------------------
st.subheader("📈 SOC Prediction Result")

if predict_btn:
    soc = model.predict([[voltage, current, temperature]])
    st.success(f"✅ Predicted State of Charge (SOC): **{soc[0]:.2f}%**")

else:
    st.info("ℹ️ Enter values in the sidebar and click **Predict SOC**")

# -----------------------------
# Visualization Section
# -----------------------------
if show_plots:
    st.subheader("📊 Battery Data Visualizations (NASA Dataset)")

    col1, col2 = st.columns(2)

    # SOC vs Voltage
    with col1:
        st.markdown("**SOC vs Voltage**")
        fig1, ax1 = plt.subplots()
        ax1.scatter(data['Voltage'], data['SOC'])
        ax1.set_xlabel("Voltage (V)")
        ax1.set_ylabel("SOC (%)")
        ax1.set_title("SOC vs Voltage")
        ax1.grid(True)
        st.pyplot(fig1)

    # SOC vs Temperature
    with col2:
        st.markdown("**SOC vs Temperature**")
        fig2, ax2 = plt.subplots()
        ax2.scatter(data['Temperature'], data['SOC'])
        ax2.set_xlabel("Temperature (°C)")
        ax2.set_ylabel("SOC (%)")
        ax2.set_title("SOC vs Temperature")
        ax2.grid(True)
        st.pyplot(fig2)

    # Actual vs Predicted SOC
    st.markdown("**Actual vs Predicted SOC**")

    X = data[['Voltage', 'Current', 'Temperature']]
    y_actual = data['SOC']
    y_pred = model.predict(X)

    fig3, ax3 = plt.subplots()
    ax3.scatter(y_actual, y_pred, alpha=0.6)
    ax3.set_xlabel("Actual SOC (%)")
    ax3.set_ylabel("Predicted SOC (%)")
    ax3.set_title("Actual vs Predicted SOC")
    ax3.grid(True)
    st.pyplot(fig3)

# -----------------------------
# Footer
# -----------------------------
st.markdown("---")
st.markdown(
    """
**Developed by Aftab Ahmed**  
AI-based EV Battery Diagnostics | NASA Dataset | Machine Learning  

🔹 *Future Scope*: SOH prediction, LSTM models, real-time BMS integration
"""
)
