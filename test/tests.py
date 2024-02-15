import unittest
from pystock.pystock import fetch_stock_data


class TestStockInfo(unittest.TestCase):
    def test_get_stock_info(self):
        self.assertRaises(TypeError, fetch_stock_data, 1, 1)
        self.assertRaises(TypeError, fetch_stock_data, "AMZN", 1.0)
        self.assertRaises(TypeError, fetch_stock_data, "AMZN", 0)
        self.assertRaises(ConnectionError, fetch_stock_data, "HELLOOOOOOOOO", 1)
