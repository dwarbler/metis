import unittest
import numpy as np
from pystock.pystock import fetch_stock_data
from pystock.pystock import calculate_black_scholes_sigma
from pystock.pystock import black_scholes_predict_next
from pystock.pystock import run_program


class TestStockInfo(unittest.TestCase):
    def test_fetch_stock_data(self):
        self.assertRaises(TypeError, fetch_stock_data, 1, 2)
        self.assertRaises(TypeError, fetch_stock_data, "AMZN", 0)
        self.assertRaises(TypeError, fetch_stock_data, "AMZN", 2.0)
        self.assertRaises(ConnectionError, fetch_stock_data, "HELLOOOOOOOOO", 2)

    def test_calculate_black_scholes_sigma(self):
        self.assertRaises(TypeError, calculate_black_scholes_sigma, 1)

    def test_black_scholes_predict_next(self):
        self.assertRaises(TypeError, black_scholes_predict_next, "1", 1.5, 1.5, 1.5)
        self.assertRaises(TypeError, black_scholes_predict_next, 1.5, "1", 1.5, 1.5)
        self.assertRaises(TypeError, black_scholes_predict_next, 1.5, 1.5, "1", 1.5)
        self.assertRaises(TypeError, black_scholes_predict_next, 1.5, 1.5, 1.5, "1")
        self.assertEqual(
            np.exp(1 - 1 / 2 + 1), black_scholes_predict_next(1.0, 1.0, 1.0, 1.0, 1.0)
        )

    def test_running_program(self):
        self.assertRaises(ConnectionError, run_program)
