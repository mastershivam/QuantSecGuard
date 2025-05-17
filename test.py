import yfinance as yf

def get_stock_data(ticker="AAPL", period="1y", interval="1h"):
    df = yf.download(ticker, period=period, interval=interval)
    df.reset_index(inplace=True)
    df["price"] = df["Close"]
    df["volume"] = df["Volume"]
    return df[["Datetime", "price", "volume"]]

df=get_stock_data()
print(df.head())