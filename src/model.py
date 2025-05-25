import sys
import os

from sklearn.svm import OneClassSVM

sys.path.append(os.path.join(os.path.dirname(__file__), 'src'))
import pandas as pd
from sklearn.ensemble import IsolationForest

def detect_anomalies(model,df, n_trees,contamination=0.01, random_state=3):
    features = df[['returns', 'volatility', 'volume']].copy()
    features['volume'] = features['volume'].ffill()

    if model=="IsolationForest":
        model = IsolationForest(
            n_estimators=n_trees,
            contamination=contamination,
            random_state=random_state,
            max_features=1.0
        )
        preds = model.fit_predict(features)
    elif model == "One Class SVM":
        model = OneClassSVM(
            nu=kwargs.get('nu', 0.05),
            kernel='rbf',
            gamma='auto'
        )
        preds = model.fit_predict(features)


    df['anomaly_score'] = preds
    df['is_anomaly'] = df['anomaly_score'] == -1
    anomalies = df[df['is_anomaly']]

    return df, anomalies


