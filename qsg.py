import pandas as pd
import numpy as np
from sklearn.ensemble import IsolationForest
import matplotlib.pyplot as plt
import yfinance as yf

data=yf.download("AAPL",period="max",interval="1d")

# Simulate financial time series ===
np.random.seed(43)
n_points = 1000

# Price = cost of a stock (around 100 with some variance based on a random number generator)
price = np.cumsum(np.random.normal(0, 1, n_points)) + 100

# Volume = quantity of the stock that is traded, 1000 is the mean, 200 is the width
volume = np.abs(np.random.normal(1000, 200, n_points))

# Spread = variance between highest buy price and lowest sell price
spread = np.abs(np.random.normal(0.5, 0.1, n_points))


# Inject synthetic anomalies
price[100:105] += 20            # price spike
volume[400:405] *= 5            # huge volume burst
spread[700:705] *= 10           # spread manipulation

# === 2. Create DataFrame ===
df = pd.DataFrame({
    'price': price,
    'volume': volume,
    'spread': spread
})

# Add features
# for each price, get the change in price from the previous price
df['returns'] = df['price'].pct_change().fillna(0)
# for each return, take a rolling window and get the standard deviation
df['volatility'] = df['returns'].rolling(window=10).std().fillna(0)

# === 3. Apply Isolation Forest ===

# Select 4 columns as features from the dataset
features = df[['returns', 'volatility', 'volume', 'spread']]
# tells the model to expect 1% outlier rate
model = IsolationForest(contamination=0.01, random_state=43)

# fits the model to the notebook and predicts whether each row is anomolous or not
df['anomaly_score'] = model.fit_predict(features)

# creates a boolean column where the output is False if there is no anomaly, and True if there is
df['is_anomaly'] = df['anomaly_score'] == -1

# === 4. Plot Results ===
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

# === 5. Output table of anomalies ===
anomalies = df[df['is_anomaly']]
print(anomalies[['price', 'volume', 'spread', 'returns', 'volatility']])