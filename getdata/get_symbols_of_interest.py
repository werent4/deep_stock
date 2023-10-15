import pandas as pd
from methods import get_data, find_interest, save_data_pickle, read_data_pickle
from tqdm import tqdm
from multiprocessing import Pool

df = pd.read_csv('nasdaq_screener_1697135861885.csv')
symbol_list = df['Symbol'].to_list()
stocks_of_interest = []

# A function for parallel processing
def process_symbol(symbol):
    try:
        temp_df = get_data(symbol)
        stocks_of_interest_temp = find_interest(-0.09, temp_df, symbol, [])
        return stocks_of_interest_temp
    except Exception as e:
        # Print the error
        print(f"Error processing symbol {symbol}: {str(e)}")
        return []  # Return an empty list in case of an error


if __name__ == '__main__':
    # Number of CPU cores to use for parallel processing
    num_cores = 8 # Adjust this according to your system

    # Create a Pool of worker processes
    with Pool(num_cores) as pool:
        # Use pool.map for parallel processing
        stocks_of_interest_temp_list = list(tqdm(pool.imap(process_symbol, symbol_list), total=len(symbol_list)))

    # Combine results from parallel processes
    for temp_list in stocks_of_interest_temp_list:
        stocks_of_interest.extend(temp_list)

    # Save the combined results in 'data.picle' and 'stocks_of_interest'
    save_data_pickle('009_min_fall_60d_13_10_2023.pickle', stocks_of_interest)

print(stocks_of_interest)
