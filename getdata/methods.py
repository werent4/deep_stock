import pandas as pd
import yfinance as yf
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

def find_interest(growth,amplitude,df,symbol,stocks_of_interest):
    """ use 'growth' to indicate the move of interest: growth = True to indicate positive change
    (use positive values of 'amplitude', for example, 0.09),
    growth = False to indicate negative change, (use negative values of 'amplitude', for example, 0.09)"""
    open_list = df["Open"].to_list()
    close_list = df["Close"].to_list()
    date_list = df.index.to_list()
    stocks_of_interest = stocks_of_interest[30:]
    length = len(open_list)
    #(B / A) — 1 = C
    if growth == False:
        highest_amplitude = [1, 1, 1]
        for i in range(length - 2):
            diff = ((open_list[i + 1]) / close_list[i]) - 1
            if diff < highest_amplitude[1]:
                highest_amplitude = [symbol, diff, date_list[i + 1]]
        if highest_amplitude[1] < amplitude:
            stocks_of_interest.append(highest_amplitude)
            print(highest_amplitude)
    else:
        highest_amplitude = [1, -1, 1]
        for i in range(length - 2):
            diff = ((open_list[i + 1]) / close_list[i]) - 1
            if diff > highest_amplitude[1]:
                highest_amplitude = [symbol, diff, date_list[i + 1]]
        if highest_amplitude[1] > amplitude:
            stocks_of_interest.append(highest_amplitude)
            print(highest_amplitude)

    return stocks_of_interest

