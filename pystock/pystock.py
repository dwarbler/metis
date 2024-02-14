import yfinance as yahooFinance
from yfinance import shared


def get_stock_info(ticker: str):
    """Retrieves stock info for inputted stock ticker

    Args:
        ticker (str): stock ticker

    Raises:
        TypeError: ticker is not a string
        ConnectionError: ticker was not a valid stock ticker

    Returns:
        yahooFinance.Ticker: information object about the ticker
    """
    if not isinstance(ticker, str):
        raise TypeError()

    stock_information = yahooFinance.Ticker(ticker)

    if stock_information.history(period="max").empty:
        raise ConnectionError("Invalid Ticker")

    return stock_information
