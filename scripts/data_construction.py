import pandas as pd
import yfinance as yf
import sys
sys.path.append('./helpers')
from data_preprocessing import data_cleaning


def data_construction_func():
    daily_data=yf.download(tickers='TSLA',interval='1d',start='2024-01-01')
    daily_data.rename(columns={'Open':'open','High':'high','Low':'low','Close':'close'},inplace=True)
    daily_data.reset_index(inplace=True,drop=False)
    daily_data=daily_data.to_numpy()
    daily_data=daily_data.tolist()
    daily_data=data_cleaning(daily_data)
    return daily_data
