# EV-Battery-SOC-Prediction
AI-based SOC prediction for EV batteries using Machine Learning
## Dataset
This project uses the NASA Lithium-Ion Battery Aging Dataset.
SOC is derived from battery capacity using:

SOC = (Current Capacity / Rated Capacity) × 100

## Exploratory Data Analysis
- SOC vs Voltage
- SOC vs Temperature
- Actual vs Predicted SOC plots

## Model Evaluation
Random Forest Regressor was selected due to its ability to model
non-linear relationships in battery sensor data.

RMSE was used as the evaluation metric.

## Future Improvements
- Integration with real-time BMS data
- LSTM-based temporal modeling
- Edge deployment on EV hardware
