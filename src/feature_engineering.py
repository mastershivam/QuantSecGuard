
# Add features
def generate_features(df):
    # for each price, get the change in price from the previous price
    df['returns'] = df['price'].pct_change().fillna(0)
    # for each return, take a rolling window and get the standard deviation
    df['volatility'] = df['returns'].rolling(window=10).std().fillna(0)

    return df