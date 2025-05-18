import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), 'src'))
import yfinance as yf

def get_stock_data(ticker,interval):


    df = yf.download(ticker, period=interval)
    df.reset_index(inplace=True)
    df.rename(columns={"Date": "Datetime"}, inplace=True)
    df["price"] = df["Close"]
    df["volume"] = df["Volume"]

    return df