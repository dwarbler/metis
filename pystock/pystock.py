import datetime as dt
import pandas as pd
from pandas_datareader import data as pdr


def fetch_stock_data(ticker: str, length: int) -> pd.DataFrame:
    """fetches pandas dataframe of stock prices for a given ticker

    Args:
        ticker (str): stock ticker
        length (int): number of days of data to fetch

    Raises:
        TypeError: incorrect/inavlid type given to function
        ConnectionError: invalid ticker given to function

    Returns:
        pd.DataFrame: dataframe containing stock data
    """
    if not isinstance(ticker, str) or not isinstance(length, int) or length < 1:
        raise TypeError()

    end = dt.datetime.now()
    start = end - dt.timedelta(days=length)

    try:
        df = pdr.get_data_yahoo(ticker, start, end)
    except Exception as e:
        raise ConnectionError("Invalid Ticker") from e

    return df
