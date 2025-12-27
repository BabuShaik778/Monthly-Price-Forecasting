# app.py
import streamlit as st
import pandas as pd
import numpy as np
import pickle
from prophet import Prophet
import matplotlib.pyplot as plt

st.set_page_config(page_title="Price Forecasting", layout="centered")

st.title("📈 Price Forecasting App")

# -------------------
# Step 1: Upload CSV
# -------------------
uploaded_file = st.file_uploader("Upload CSV file with columns: 'date', 'avg_monthly_price'", type=['csv'])

if uploaded_file:
    df = pd.read_csv(uploaded_file)
    st.subheader("Raw Data")
    st.dataframe(df.head())

    # Preprocess
    df['date'] = pd.to_datetime(df['date'])
    df.sort_values('date', inplace=True)
    df.rename(columns={'date': 'ds', 'avg_monthly_price': 'y'}, inplace=True)
    df['y'] = df['y'].fillna(method='ffill')

    # -------------------
    # Step 2: Load Model
    # -------------------
    try:
        with open('prophet_model.pkl', 'rb') as f:
            model = pickle.load(f)
        st.success("Model loaded successfully!")
    except FileNotFoundError:
        st.error("Pickle model not found! Train and save the model first.")
        st.stop()

    # -------------------
    # Step 3: Forecast
    # -------------------
    periods = st.slider("Select number of months to forecast:", min_value=1, max_value=24, value=12)
    future = model.make_future_dataframe(periods=periods, freq='M')
    forecast = model.predict(future)

    st.subheader("Forecasted Prices")
    st.dataframe(forecast[['ds', 'yhat']].tail(periods))

    # Trend suggestion
    forecast_next = forecast[['ds', 'yhat']].tail(periods)
    forecast_next['trend'] = np.where(forecast_next['yhat'].diff() > 0, 'Increase', 'Decrease')
    st.subheader("Forecast Trend")
    st.dataframe(forecast_next)

    # -------------------
    # Step 4: Plot Forecast
    # -------------------
    st.subheader("Forecast Plot")
    plt.figure(figsize=(12,6))
    plt.plot(df['ds'], df['y'], label='Historical Price')
    plt.plot(forecast['ds'], forecast['yhat'], label='Forecast', color='red')
    plt.xlabel('Date')
    plt.ylabel('Price')
    plt.legend()
    st.pyplot(plt)
