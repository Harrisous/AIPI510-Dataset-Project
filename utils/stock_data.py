import yfinance as yf
import pandas as pd
import os

def get_stock_price(ticker, start_date, end_date, interval="1d"):
    '''
    This function gets the stock price of a given ticker from Yahoo Finance
    :param ticker: The ticker of the stock
    :param start_date: The start date of the data
    :param end_date: The end date of the data
    :param interval: The interval of the data
    :return: The stock price data of the given ticker
    '''
    stock = yf.Ticker(ticker)
    stock_data = stock.history(start=start_date, end=end_date, interval=interval, auto_adjust=False, actions=True)
    return stock_data

def get_sp500_tickers():
    '''
    This function gets the list of stock tickers in the S&P 500 index
    :return: A list of stock tickers in the S&P 500 index
    '''
    url = 'https://en.wikipedia.org/wiki/List_of_S%26P_500_companies'
    table = pd.read_html(url, header=0)
    sp500_table = table[0]
    sp500_tickers = sp500_table['Symbol'].tolist()
    return sp500_tickers

def collect_all_data(start_date="1980-01-01", end_date="2023-12-31", interval="1d"):
    '''
    This function collects stock price data of all the target tickers inside target list of indices
    :param target: The list of list of indices
    :param start_date: The start date of the data
    :param end_date: The end date of the data
    :return: The stock price data of all the target tickers
    '''
    target=["^GSPC", "^DJI", "^IXIC", "^RUT"]
    # step 1: get the list of tickers for each index
    for index in target:
        # data collection and processing
        df = get_stock_price(index, start_date, end_date, interval=interval)
        df.reset_index(inplace=True)
        df["Date"] = pd.to_datetime(df["Date"]).dt.strftime('%Y-%m-%d')

        path = os.path.join("data", "indices", f"{index}.csv")
        if os.path.exists(path):
            os.remove(path)    
        df.to_csv(path, index=False)
    print("Index Saved to data/indices")

    # step 2: get the list of tickers for S&P 500
    target_tickers = get_sp500_tickers()

    # step 3: get the stock price data for each ticker
    for ticker in target_tickers:
        df = get_stock_price(ticker, start_date, end_date, interval=interval)
        df.reset_index(inplace=True)
        df["Date"] = pd.to_datetime(df["Date"]).dt.strftime('%Y-%m-%d')

        path = os.path.join("data", "stocks", f"{ticker}.csv")
        if os.path.exists(path):
            os.remove(path)
        df.to_csv(path, index=False)
    print("Component Stock Saved to data/stocks")

