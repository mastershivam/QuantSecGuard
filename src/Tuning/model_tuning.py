import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from Tuning import one_class_svm, isolation_forest
from utils import generate_features, inject_synthetic_anomalies
import numpy as np

import pandas as pd

# Example dummy data to simulate a price/volume time series
df = pd.DataFrame({
    "Datetime": pd.date_range(start="2023-01-01", periods=100, freq="D"),
    "price": np.random.normal(loc=150, scale=5, size=100),
    "volume": np.random.randint(1000, 5000, size=100)
})

df = inject_synthetic_anomalies(df)
df = generate_features(df)

models = {
    1: ("Isolation Forest", isolation_forest),
    2: ("One Class SVM", one_class_svm)
}

choice = int(input("Choose a model: 1=IsolationForest, 2=OneClassSVM: "))

model_name, module = models[choice]
print(f"Tuning {model_name}...")

result = module.tune(df)
print(result.best_params_)