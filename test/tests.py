import unittest
from pystock.pystock import fetch_stock_data
from pystock.pystock import calculate_black_scholes_sigma


class TestStockInfo(unittest.TestCase):
    def test_fetch_stock_data(self):
        self.assertRaises(TypeError, fetch_stock_data, 1, 2)
        self.assertRaises(TypeError, fetch_stock_data, "AMZN", 0)
        self.assertRaises(TypeError, fetch_stock_data, "AMZN", 2.0)
        self.assertRaises(ConnectionError, fetch_stock_data, "HELLOOOOOOOOO", 2)

    def test_calculate_sigma(self):
        self.assertEqual(1.0, calculate_black_scholes_sigma(fetch_stock_data("AMZN", 10)))
