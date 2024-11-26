import yfinance as yf
import pandas as pd
import os

def load_bond_yield_data(ticker, start="1980-01-01", end="2020-12-31", interval="1d"):
    bond_data = yf.download(ticker, start=start, end=end, interval=interval)
    return bond_data

def save_bond_yield_data(start="1980-01-01", end="2020-12-31", interval="1d"):
    tickers = {
        "13-Week Treasury Bill": "^IRX",
        "5-Year Treasury Note": "^FVX",
        "10-Year Treasury Note": "^TNX",
        "30-Year Treasury Bond": "^TYX"
    }

    for name, ticker in tickers.items():
        df = load_bond_yield_data(ticker, start=start, end=end, interval=interval)
        df.reset_index(inplace=True)
        df["Date"] = pd.to_datetime(df["Date"]).dt.strftime('%Y-%m-%d')
        path = os.path.join("data", "bonds", f"{ticker}.csv")
        if os.path.exists(path):
            os.remove(path)
        df.to_csv(path, index=False)
    print("Data saved to data/bonds")


