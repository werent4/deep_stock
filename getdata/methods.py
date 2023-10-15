import pandas as pd
import yfinance as yf
import yahoofinancials
from yahoofinancials import YahooFinancials
import math
import pickle

def save_data_pickle(filename,data):
    with open(filename, 'wb') as handle:
        pickle.dump(data, handle, protocol=pickle.HIGHEST_PROTOCOL)

def read_data_pickle(filename):
    with open(filename, 'rb') as handle:
        data = pickle.load(handle)
    return data


def get_data(symbol):
    temp_df = yf.download(symbol, period = '3mo',
                          # start='2023-08-12',
                          # end='2023-10-12',
                          interval='1d',
                          progress=False,
    )
    return temp_df

def find_interest(amplitude,df,symbol,stocks_of_interest):
    open_list = df["Open"].to_list()
    close_list = df["Close"].to_list()
    date_list = df.index.to_list()
    stocks_of_interest = stocks_of_interest[30:]
    length = len(open_list)
    #(B / A) — 1 = C
    smallest_diff = [1,1,1]
    for i in range(length-2):
        diff = ((open_list[i+1])/close_list[i]) - 1
        if diff < smallest_diff[1]:
            smallest_diff = [symbol,diff,date_list[i+1]]
    if smallest_diff[1] < amplitude:
        stocks_of_interest.append(smallest_diff)
        print(smallest_diff)

    return stocks_of_interest

