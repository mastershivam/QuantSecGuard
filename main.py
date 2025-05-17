# main.py
import pandas as pd
from src.data_loader import get_stock_data
from src.feature_engineering import generate_features
from src.model import detect_anomalies
from src.visualise import plot_anomalies

n_trees=300

def main():
    # 1. Load data
    print("📥 Loading stock data...")
    df = get_stock_data(ticker="AAPL", period="6mo", interval="1h")

    # 2. Feature engineering
    print("🧠 Generating features...")
    df = generate_features(df)

    # 3. Train and detect anomalies
    print("🔍 Running anomaly detection...")
    df, anomaly= detect_anomalies(df,n_trees)

    # 4. Output and plot
    print(f"✅ Found {len(anomaly)} anomalies.")
    plot_anomalies(df)

if __name__ == "__main__":
    main()