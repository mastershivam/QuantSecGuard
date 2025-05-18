import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), 'src'))

import numpy as np
import pandas as pd
from sklearn.ensemble import IsolationForest
from sklearn.metrics import precision_score, recall_score, f1_score
from itertools import product

def inject_synthetic_anomalies(df, n=10):
    df = df.copy()
    anomaly_indices = np.random.choice(df.index[20:-20], n, replace=False)
    df.loc[anomaly_indices, 'volume'] *= 10  # Inject a spike
    df['label'] = 0
    df.loc[anomaly_indices, 'label'] = 1
    return df

def generate_features(df):
    df['returns'] = df['price'].pct_change().fillna(0)
    df['volatility'] = df['returns'].rolling(window=10).std().fillna(0)
    df['volume'] = df['volume'].fillna(method='ffill')
    return df.dropna()

def evaluate_model(y_true, y_pred):
    precision = precision_score(y_true, y_pred, zero_division=0)
    recall = recall_score(y_true, y_pred, zero_division=0)
    f1 = f1_score(y_true, y_pred, zero_division=0)
    return precision, recall, f1

def tune_isolation_forest(df):
    # Grid of parameters
    param_grid = {
        'n_estimators': [100, 200,300,400],
        'contamination': [0.005, 0.01, 0.02, 0.03, 0.04],
        'max_features': [1.0, 0.75,0.5],
    }

    results = []

    for n_est, cont, max_feat in product(
            param_grid['n_estimators'],
            param_grid['contamination'],
            param_grid['max_features']):

        features = df[['returns', 'volatility', 'volume']]
        model = IsolationForest(
            n_estimators=n_est,
            contamination=cont,
            max_features=max_feat,
            random_state=42
        )

        y_pred = model.fit_predict(features)
        y_pred = np.where(y_pred == -1, 1, 0)  # Convert to binary

        precision, recall, f1 = evaluate_model(df['label'], y_pred)
        results.append(((n_est, cont, max_feat), precision, recall, f1))

    return sorted(results, key=lambda x: x[3], reverse=True)  # Sort by F1

# === EXAMPLE USAGE ===
if __name__ == "__main__":
    np.random.seed(42)

    # Simulate data
    n = 1000
    price = np.cumsum(np.random.normal(0, 1, n)) + 100
    volume = np.abs(np.random.normal(1000, 200, n))
    df = pd.DataFrame({'price': price, 'volume': volume})

    # Inject anomalies + features
    df = inject_synthetic_anomalies(df)
    df = generate_features(df)

    # Tune model
    results = tune_isolation_forest(df)

    # Show top 5 results
    for (params, prec, rec, f1) in results[:5]:
        print(f"Params: n_estimators={params[0]}, contamination={params[1]}, max_features={params[2]}")
        print(f"→ Precision: {prec:.2f}, Recall: {rec:.2f}, F1: {f1:.2f}\n")