from tqdm import tqdm
from methods import read_data_pickle
from multiprocessing import Pool
import yfinance as yf
import os

def get_data(symbol):
    try:
        temp_df = yf.download(symbol,
                             start='2023-08-15',
                             end='2023-10-14',
                             interval='1d',
                             progress=False,
                            )
        return temp_df
    except Exception as e:
        # Print the error
        print(f"Error processing symbol {symbol}")
        return None

def process(symbol):
    data = get_data(symbol)
    if data is not None:
        output_dir = 'datasets\data_raw_60d_1d'
        os.makedirs(output_dir, exist_ok=True)
        output_path = os.path.join(output_dir, f'{symbol}.csv')
        data.to_csv(output_path)

symbol_list = read_data_pickle('009_min_fall_60d_13_10_2023.pickle')
symbol_list = [i[0] for i in symbol_list]

if __name__ == '__main__':
    # Number of CPU cores to use for parallel processing
    num_cores = 8 # Adjust this according to your system

    # Create a Pool of worker processes
    with Pool(num_cores) as pool:
        # Use pool.map for parallel processing
        list(tqdm(pool.imap(process, symbol_list), total=len(symbol_list)))
