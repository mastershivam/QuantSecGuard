import sys
import os
import requests
import pandas as pd
sys.path.append(os.path.join(os.path.dirname(__file__), 'src'))
import yfinance as yf

def get_stock_data(ticker,period,interval):


    df = yf.download(ticker, period=period,interval=interval)
    df.reset_index(inplace=True)
    df.rename(columns={"Date": "Datetime"}, inplace=True)
    df["price"] = df["Close"]
    df["volume"] = df["Volume"]

    return df

def get_binance_data(symbol='BTCUSDT', interval='1m', limit=500):
    url = "https://api.binance.com/api/v3/klines"
    params = {'symbol': symbol, 'interval': interval, 'limit': limit}
    response = requests.get(url, params=params)
    data = response.json()

    df = pd.DataFrame(data, columns=[
        'Open time', 'Open', 'High', 'Low', 'Close', 'Volume',
        'Close time', 'Quote asset volume', 'Number of trades',
        'Taker buy base', 'Taker buy quote', 'Ignore'
    ])
    df['Open time'] = pd.to_datetime(df['Open time'], unit='ms')
    df['price'] = df['Close'].astype(float)
    df['volume'] = df['Volume'].astype(float)
    df['Datetime'] = df['Open time']
    return df[['Datetime', 'price', 'volume']]