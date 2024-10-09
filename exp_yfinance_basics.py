'''This demo is modified from the example given in following '''
# https://www.geeksforgeeks.org/how-to-use-yfinance-api-with-python/

import yfinance as yf

'''Part 1 single ticker'''
# Define the ticker symbol
ticker_symbol = "AAPL"

# Create a Ticker object
ticker = yf.Ticker(ticker_symbol)

# print(ticker.info)

# # Fetch historical market data
# # Interval setting: “1m”, “2m”, “5m”, “15m”, “30m”, “60m”, “90m”, “1h”, “1d”, “5d”, “1wk”, “1mo”, “3mo”
# historical_data = ticker.history(period="1y")  # data for the last year
historical_data = ticker.history(start="2024-10-01", end="2024-10-08", interval="1d", auto_adjust=False, actions=False)  # auto_adjust = false: show [adj. close]; actions = Ture: show [dividents] and [stock splits]

# historical_data = ticker.history(period="max", interval="1d") # already loaded to pd dataframe
print("Historical Data:")
print(type(historical_data))
print(historical_data)

# # Fetch basic financials
# financials = ticker.financials
# print("\nFinancials:")
# print(financials)

# # Fetch stock actions like dividends and splits
# actions = ticker.actions
# print("\nStock Actions:")
# print(actions)

# download function
data = yf.download("AAPL", start="2024-10-01", end="2024-10-08")
print(type(data))
print(data)

'''Part 2 multiple ticker'''
# tickers = yf.Tickers('msft aapl goog')

# # access each ticker using (example)
# tickers.tickers['MSFT'].info
# tickers.tickers['AAPL'].history(period="1mo")
# tickers.tickers['GOOG'].actions

# download function
# data = yf.download("AMZN AAPL GOOG", start="2017-01-01", end="2017-04-30")