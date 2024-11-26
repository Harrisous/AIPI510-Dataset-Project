import unittest
from unittest.mock import patch, MagicMock
import pandas as pd
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from utils.stock_data import get_stock_price, get_sp500_tickers

class TestStockData(unittest.TestCase):

    @patch('utils.stock_data.yf.Ticker')
    def test_get_stock_price(self, mock_ticker):
        # Mock the stock history data
        mock_stock = MagicMock()
        mock_stock.history.return_value = pd.DataFrame({
            'Date': pd.date_range(start='2020-01-01', periods=5, freq='D'),
            'Open': [1, 2, 3, 4, 5],
            'High': [2, 3, 4, 5, 6],
            'Low': [0.5, 1.5, 2.5, 3.5, 4.5],
            'Close': [1.5, 2.5, 3.5, 4.5, 5.5],
            'Adj Close': [1.5, 2.5, 3.5, 4.5, 5.5],
            'Volume': [1000, 2000, 3000, 4000, 5000]
        })
        mock_ticker.return_value = mock_stock

        # Call the function
        ticker = 'AAPL'
        start_date = '2020-01-01'
        end_date = '2020-01-05'
        interval = '1d'
        result = get_stock_price(ticker, start_date, end_date, interval)

        # Check the result
        self.assertEqual(len(result), 5)
        self.assertIn('Date', result.columns)
        self.assertIn('Open', result.columns)

    @patch('utils.stock_data.pd.read_html')
    def test_get_sp500_tickers(self, mock_read_html):
        # Mock the HTML table data
        mock_read_html.return_value = [pd.DataFrame({
            'Symbol': ['AAPL', 'MSFT', 'GOOGL']
        })]

        # Call the function
        result = get_sp500_tickers()

        # Check the result
        self.assertEqual(len(result), 3)
        self.assertIn('AAPL', result)
        self.assertIn('MSFT', result)
        self.assertIn('GOOGL', result)


if __name__ == '__main__':
    unittest.main()