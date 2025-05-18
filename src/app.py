import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), 'src'))

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from data_loader import get_stock_data
from feature_engineering import generate_features
from model import detect_anomalies

st.set_page_config(page_title="QuantSecGuard", layout="centered")
st.title("QuantSecGuard - Market Anomaly Detector")

# Sidebar inputs
ticker = st.sidebar.text_input("Enter Stock Ticker", "AAPL")
interval = st.sidebar.selectbox("Interval", ('1d', '5d', '1mo', '3mo', '6mo', '1y', '2y', '5y', '10y', 'ytd', 'max'))
n_trees = st.sidebar.text_input("Number of trees", "300")
n_trees= int(n_trees)
if st.sidebar.button("Run Detection"):
    with st.spinner("Fetching and analyzing data..."):
        try:
            df = get_stock_data(ticker=ticker, interval=interval)
            df = generate_features(df)
            df, anomalies = detect_anomalies(df,n_trees)

            # Plotting
            fig, ax = plt.subplots(figsize=(12, 6))
            ax.plot(df["Datetime"], df["price"], label="Price", color="blue")
            ax.scatter(anomalies["Datetime"], anomalies["price"], color="red", label="Anomalies", marker="x")
            ax.set_title(f"Anomalies in {ticker} Price")
            ax.set_xlabel("Time")
            ax.set_ylabel("Price")
            ax.legend()
            ax.grid(True)
            st.pyplot(fig)

            st.subheader("Anomaly Table")
            st.dataframe(anomalies[["Datetime", "price", "volume", "returns", "volatility"]])
        except Exception as e:
            st.error(f"Error during analysis: {e}")