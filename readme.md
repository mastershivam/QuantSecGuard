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

## Project Structure

```
QuantSecGuard/
├── data/
├── notebooks/
├── src/
│   ├── data_loader.py
│   ├── feature_engineer.py
│   ├── model.py
│   ├── visualize.py
├── main.py
├── tune_model.py
├── README.md
└── requirements.txt
```

##  How to Run

1. Clone the repo
2. Install requirements
```bash
pip install -r requirements.txt
```
3. Run main pipeline:
```bash
python main.py
```
4. To run model tuning:
```bash
python tune_model.py
```

## Example Output

Demo Anomaly Chart![img.png](img.png)

## Future Enhancements

- Streamlit dashboard
- Real-time Binance data ingestion
- Extended model options (Autoencoder, One-Class SVM)
- Alerting & scoring system for anomalies

---

### 💼 Built by Shivam Lakhani

This project showcases skills in ML, data engineering, and market analytics — designed for roles in fintech, quant research, and ML security.

Feel free to fork, play, and contribute!


