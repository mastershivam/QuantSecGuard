
from sklearn.ensemble import IsolationForest






#
# === 5. Output table of anomalies ===
anomalies = df[df['is_anomaly']]
print(anomalies[['price', 'volume','returns', 'volatility']])