import unittest
import yfinance as yahooFinance
from pystock.pystock import get_stock_info


class TestStockInfo(unittest.TestCase):
    def test_get_stock_info(self):
        self.assertRaises(TypeError, get_stock_info, 1)
        self.assertRaises(ConnectionError, get_stock_info, "HELLOOOOOOOOO")
        self.assertEqual(yahooFinance.Ticker("AMZN").info, get_stock_info("AMZN").info)
