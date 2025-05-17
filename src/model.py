
import pandas as pd
from sklearn.ensemble import IsolationForest

def detect_anomalies(df, n_trees,contamination=0.01, random_state=3):
    features = df[['returns', 'volatility', 'volume']].copy()
    features['volume'] = features['volume'].fillna(method='ffill')

    model = IsolationForest(
        n_estimators=n_trees,
        contamination=contamination,
        random_state=random_state,
        max_features=1.0
    )

    df['anomaly_score'] = model.fit_predict(features)
    df['is_anomaly'] = df['anomaly_score'] == -1

    anomalies = df[df['is_anomaly']]
    return df, anomalies
