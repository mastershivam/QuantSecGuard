import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), 'src'))
from utils import *
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
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

def graph_plotting(df,anomalies,source,interval_period,stock_crypto):
    fig, ax = plt.subplots(figsize=(12, 6))
    ax.plot(df["Datetime"], df["price"], label="Price", color="blue")
    ax.scatter(anomalies["Datetime"], anomalies["price"], color="red", label="Anomalies", marker="x")

    x_format = get_time_format(interval_period)
    ax.xaxis.set_major_formatter(mdates.DateFormatter(x_format))
    plt.xticks(rotation=45)

    plt.xticks(rotation=45)
    if source == "Crypto":
        ax.set_title(f"Anomalies in {stock_crypto} Pair")
    elif source == "Stock":
        ax.set_title(f"Stock Price in {stock_crypto} Pair")
    ax.set_title(f"Anomalies in {stock_crypto} Price")

    ax.set_ylabel("Price")
    ax.legend()
    ax.grid(True)
    return fig, ax