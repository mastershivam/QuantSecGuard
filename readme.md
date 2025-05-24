# QuantSecGuard

**QuantSecGuard** is an ML-powered anomaly detection system for financial time series — built at the intersection of quantitative finance, cybersecurity, and machine learning.

Explore this app deployed here: https://quantsecguard-hxshnbl4mxbavkgcotteor.streamlit.app/

## Overview

This project applies unsupervised learning to detect unusual behavior in market data, simulating real-world use cases like:

- Market manipulation monitoring (e.g., spoofing, pump-and-dump)
- Strategy debugging (e.g., signal decay, execution drift)
- Risk anomaly detection

## Techniques Used

- **Isolation Forest** for anomaly detection
- Feature engineering (returns, volatility, volume)
- Parameter tuning via F1-score with synthetic anomaly injection
- Real-time data ingestion using `yfinance` (stocks)
- Real-time data ingestion using `Binance` (crypto)
- Modular time series selection for all stocks/cryptos
- Real-time Binance data ingestion

## Project Structure

```
QuantSecGuard/
├── data/
├── .devcontainer/
├── .venv/
├── notebook/
├── src/
│   ├── __init__.py
│   ├── app.py
│   ├── data_loader.py
│   ├── feature_engineer.py
│   ├── model.py
│   ├── model_tuning.py
│   ├── utils.py
│   ├── visualise.py
├── main.py
├── img.png
├── qsg.py
├── qsg_w_data.py
├── README.md
├── test.py
└── requirements.txt

```


## Example Output

Demo Anomaly Chart![img.png](img.png)

## Future Enhancements

- Extended model options (Autoencoder, One-Class SVM)
- Alerting & scoring system for anomalies
- Codebase cleanup and refactoring
- Add dropdown menus for selecting common crypto pairs and stock tickers

---

### 💼 Built by Shivam Lakhani

This project showcases skills in ML, data engineering, and market analytics — designed for roles in fintech, quant research, and ML security.

Feel free to fork, play, and contribute!


