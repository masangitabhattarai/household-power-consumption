import streamlit as st
import pandas as pd
import joblib
import os
import matplotlib.pyplot as plt

# Load Saved Model

model_path = os.path.join("notebook", "prophet_hourly_model.pkl")  # Corrected path
if not os.path.exists(model_path):
    st.error(f" Model file not found at: {model_path}")
    st.stop()

model = joblib.load(model_path)

# App Title

st.title("⚡ Time Series Forecasting with Prophet")
st.write("This app uses a **saved Prophet model** for forecasting and residual analysis.")

# Upload Dataset (Optional)

uploaded_file = st.file_uploader("Upload your dataset (CSV with 'ds' and 'y')", type=["csv"])

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    df['ds'] = pd.to_datetime(df['ds'])  # Ensure datetime
    st.success("Dataset uploaded successfully!")
else:
    st.info("Using model’s training data.")
    try:
        df = model.history.copy()
    except Exception as e:
        st.error("Could not load training history from model.")
        st.stop()

# Forecast Future

periods = st.slider("Select forecast horizon (hours)", 1, 168, 24)  # up to 7 days
future = model.make_future_dataframe(periods=periods, freq='H')
forecast = model.predict(future)

# Plot Forecast

st.subheader("Forecast Plot")
fig1, ax1 = plt.subplots(figsize=(10, 5))
ax1.plot(df['ds'], df['y'], label="Historical")
ax1.plot(forecast['ds'], forecast['yhat'], label="Forecast")
ax1.fill_between(forecast['ds'], forecast['yhat_lower'], forecast['yhat_upper'], alpha=0.3, label="Confidence Interval")
ax1.legend()
st.pyplot(fig1)

# Residual Analysis

st.subheader("Residual Analysis")

# Filter forecast to only include the training period
forecast_train = forecast[forecast['ds'] <= df['ds'].max()].copy() 

# Merge df and forecast_train on the 'ds' column
merged_df = df.merge(forecast_train, on='ds', how='inner')

# Calculate residuals from the merged dataframe
# 'y' is from df, 'yhat' is from forecast_train
residuals = merged_df['y'].values - merged_df['yhat'].values

fig2, ax2 = plt.subplots(figsize=(10, 4))
ax2.plot(merged_df['ds'], residuals, marker='o', linestyle='-', label="Residuals")
ax2.axhline(0, color="red", linestyle="--")
ax2.set_xlabel("Date")
ax2.set_ylabel("Residual (y - yhat)")
ax2.legend()
st.pyplot(fig2)

# Show Forecast Table

st.subheader("Forecasted Values")
st.dataframe(forecast[['ds', 'yhat', 'yhat_lower', 'yhat_upper']].tail(periods))