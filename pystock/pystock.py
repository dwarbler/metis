import datetime as dt
import pandas as pd
from pandas_datareader import data as pdr


def fetch_stock_data(ticker: str, length: int) -> pd.DataFrame:
    if not isinstance(ticker, str) or not isinstance(length, int) or length < 1:
        raise TypeError()

    end = dt.datetime.now()
    start = end - dt.timedelta(days=length)

    try:
        df = pdr.get_data_yahoo(ticker, start, end)
    except Exception as e:
        raise ConnectionError("Invalid Ticker") from e

    return df
