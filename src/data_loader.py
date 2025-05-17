
import yfinance as yf

def get_stock_data(ticker,period,interval):

    df = yf.download(ticker, period=period, interval=interval)
    df.reset_index(inplace=True)
    df["price"] = df["Close"]
    df["volume"] = df["Volume"]

    return df