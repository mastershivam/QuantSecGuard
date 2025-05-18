import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), 'src'))

import matplotlib.pyplot as plt

def plot_anomalies(df):

    plt.figure(figsize=(12, 6))
    plt.plot(df['price'], label='Price')
    plt.scatter(df[df['is_anomaly']].index, df[df['is_anomaly']]['price'],
                color='red', label='Anomalies', marker='x')
    plt.title('Market Price with Anomalies Detected')
    plt.legend()
    plt.xlabel('Time')
    plt.ylabel('Price')
    plt.grid(True)
    plt.tight_layout()
    plt.show()
