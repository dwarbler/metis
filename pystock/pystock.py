import yfinance as yahooFinance


def get_stock_info(ticker: str):
    if isinstance(ticker, str):
        raise TypeError()

    try:
        stock_information = yahooFinance.Ticker(ticker)
    except Exception as e:
        raise ConnectionError("Failed to retrieve stock data") from e

    return stock_information
