# 🔋 EV Battery State of Charge (SOC) Prediction using AI

## 📌 Overview

This project focuses on **accurate estimation of the State of Charge (SOC)** of an Electric Vehicle (EV) battery using **Artificial Intelligence and Machine Learning**. SOC estimation is a critical component of an EV **Battery Management System (BMS)**, as it directly affects range prediction, charging decisions, and user confidence.

The system is developed using **real NASA lithium-ion battery data** and is deployed as an **interactive Streamlit application** for real-time SOC prediction and visualization.

---

## 🎯 Problem Statement

In Electric Vehicles, inaccurate SOC estimation can lead to:

* Range anxiety for users
* Inefficient charging strategies
* Increased risk of battery misuse

Traditional SOC estimation techniques rely on fixed models and sensors, which may not adapt well to non-linear battery behavior. The objective of this project is to apply **machine learning** to improve SOC estimation accuracy using real sensor data.

---

## 🧠 Methodology

1. **Dataset Selection**: Used the **NASA Lithium-Ion Battery Dataset**, a widely accepted dataset in battery research.
2. **Data Preprocessing**: Selected relevant sensor parameters such as voltage, current, and temperature.
3. **SOC Derivation**: Since SOC is not directly provided in the dataset, it was derived using a **time-based normalization approach** during discharge cycles.
4. **Model Training**: Trained a **Random Forest Regressor** to capture non-linear battery characteristics.
5. **Evaluation & Visualization**: Evaluated model performance using RMSE and visual analysis.
6. **Deployment**: Deployed the trained model using **Streamlit** for real-time prediction.

---

## 📊 Dataset Description

**Source**: NASA Lithium-Ion Battery Aging Dataset

**Input Features**:

* Battery Voltage (V)
* Battery Current (A)
* Battery Temperature (°C)

**Target Variable**:

* State of Charge (SOC %)

> 📌 *Note*: SOC was derived using time normalization during discharge, which is a commonly used approximation in academic battery diagnostics when direct SOC labels are unavailable.

---

## 🤖 Machine Learning Model

* **Algorithm**: Random Forest Regressor
* **Why Random Forest?**

  * Handles non-linear relationships effectively
  * Robust to noisy sensor data
  * Suitable for small-to-medium sized experimental datasets

The trained model is serialized using **joblib** and reused during deployment to ensure fast and consistent predictions.

---

## 📈 Exploratory Data Analysis (EDA)

The following visualizations were used to validate battery behavior and model performance:

* SOC vs Voltage
* SOC vs Temperature
* Actual SOC vs Predicted SOC

These plots confirm the physical relationship between SOC and battery parameters and help assess model accuracy.

---

## 🖥️ Deployment (Streamlit)

The SOC prediction model is deployed using **Streamlit**, providing:

* User-friendly input interface
* Real-time SOC prediction
* Integrated data visualizations

### ▶️ Run Locally

```bash
pip install -r requirements.txt
streamlit run app.py
```

---

## 🚀 Future Scope

* State of Health (SOH) estimation
* LSTM-based time-series modeling for SOC
* Integration with real-time EV Battery Management Systems (BMS)

---

## 👤 Author

**Aftab Ahmed**
AI & Machine Learning | EV Battery Diagnostics

---

## ⭐ Key Takeaway

This project demonstrates how **AI can enhance EV battery diagnostics** by improving SOC estimation accuracy using real experimental data, robust machine learning models, and interactive deployment.
