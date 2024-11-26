import yfinance as yf
import os
import pandas as pd


def load_data(ticker, start="1980-01-01", end="2020-12-31", interval="1d"):
    data = yf.download(ticker, start=start, end=end, interval=interval)
    return data

def save_fx_data(start="1980-01-01", end="2020-12-31", interval="1d"):
    exchange_rate_tickers = {
        "Euro to US Dollar": "EURUSD=X",
        "Japanese Yen to US Dollar": "JPYUSD=X",
        "British Pound to US Dollar": "GBPUSD=X",
        "Australian Dollar to US Dollar": "AUDUSD=X",
        "Canadian Dollar to US Dollar": "CADUSD=X",
        "Swiss Franc to US Dollar": "CHFUSD=X"
    }

    for name, ticker in exchange_rate_tickers.items():
        df = load_data(ticker, start=start, end=end, interval=interval)
        df.reset_index(inplace=True)
        df["Date"] = pd.to_datetime(df["Date"]).dt.strftime('%Y-%m-%d')

        path = os.path.join("data", "fx", f"{ticker}.csv")
        if os.path.exists(path):
            os.remove(path)
        df.to_csv(path, index=False)
    print(f"Exchange rate data saved to data/fx")