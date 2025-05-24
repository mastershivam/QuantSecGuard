#imports
import sys
import os
from datetime import datetime
import time
sys.path.append(os.path.join(os.path.dirname(__file__), 'src'))

import streamlit as st
import matplotlib.pyplot as plt
from data_loader import get_stock_data
from feature_engineering import generate_features
from model import detect_anomalies
from data_loader import get_binance_data

from visualise import graph_plotting
from utils import *

st.set_page_config(page_title="QuantSecGuard", layout="centered")
st.title("QuantSecGuard - Market Anomaly Detector")

# Sidebar inputs
source = st.sidebar.radio("Data Source", ["Stock", "Crypto"])
if source == "Crypto":
    crypto_symbol = st.sidebar.text_input("Crypto Pair", "BTCGBP")
    crypto_interval = st.sidebar.selectbox("Crypto Interval", ["1m", "5m", "15m", "1h", "4h", "1d"])
    limit = st.sidebar.slider("Number of data points", min_value=50, max_value=1000, value=500, step=50)

if source == "Stock":
    stock_ticker = st.sidebar.text_input("Enter Stock Ticker", "AAPL")
    stock_period = st.sidebar.selectbox("Stock Period", list(valid_period_interval_map.keys()))
    stock_interval = st.sidebar.selectbox("Select Interval", valid_period_interval_map[stock_period])

n_trees = st.sidebar.text_input("Number of trees", "300")
n_trees= int(n_trees)


live_update = st.sidebar.checkbox("🔄 Enable Live Update")
refresh_seconds = st.sidebar.number_input("Update every (seconds)", min_value=1, max_value=300, value=60, step=10)

# Stock specific inputs
if source == "Stock":
    start, end = estimate_date_range(stock_period)
    st.caption(f"📆 Estimated Date Range: {start} → {end}")

# Crypto specific inputs
elif source == "Crypto":
    start, end,duration = estimate_crypto_date_range(crypto_interval, limit)
    st.caption(f"📊 {limit} data points over ~{duration}")
    st.caption(f"📆 Estimated Date Range: {start} → {end}")




# data pulling logic
if st.sidebar.button("Run Detection") or live_update:
    while True:
        with st.spinner("Fetching and analyzing data..."):
            try:
                if source=="Stock":
                    df = get_stock_data(ticker=stock_ticker, period=stock_period,interval=stock_interval)
                    df = generate_features(df)
                    df, anomalies = detect_anomalies(df,n_trees)
                elif source=="Crypto":
                    df = get_binance_data(symbol=crypto_symbol, interval=crypto_interval,limit=limit)
                    df = generate_features(df)
                    df, anomalies = detect_anomalies(df,n_trees)
                st.info(f"Pulled {len(df)} data points for analysis.")


                # Plotting variables
                interval_period=crypto_interval if source=="Crypto" else stock_period
                stock_crypto = crypto_symbol if source == "Crypto" else stock_ticker


                # Calling the Plotting function
                fig,ax=graph_plotting(df,anomalies,source,interval_period,stock_crypto)

                #Streamlabs formatting and graph outputs

                st.pyplot(fig)
                st.subheader("Anomaly Table")
                st.dataframe(anomalies[["Datetime", "price", "volume", "returns", "volatility"]])
                st.success("✅ Analysis complete")
                st.caption(f"📈 Last updated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")

            # Exception error handling
            except Exception as e:
                st.error(f"Error during analysis: {e}")

        # Live Update fallback to prevent looping
        if live_update:
            time.sleep(refresh_seconds)
            st.rerun()
        else:
            break