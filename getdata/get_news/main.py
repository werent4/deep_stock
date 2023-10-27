import os
import json
from datetime import datetime
from multiprocessing import Pool
from get_news_methods import *

#! important
# need adjustment for your self
path_to_news_folder = r'C:\Users\werent4\Desktop\deep_stock\datasets\comp_news'
comanies_file_path = r'C:\Users\werent4\Desktop\deep_stock\datasets\data_raw_60d_1d'


full_path_list = get_list_companies(comanies_file_path)

def process_company_date(company_date):
    '''
    Function processes and retrieves news data for a specific company and date, saving it to a JSON file. 
    '''
    path, date = company_date # extract path to csv file and date from file
    name = get_comp_name(path) # get name based on csv file name
    directory_path = os.path.join(path_to_news_folder, name) # create directory path for specific company

    if not os.path.exists(directory_path):
        os.makedirs(directory_path) # create directory for specific company

    date = datetime.strptime(date, '%Y-%m-%d').date()
    output_json_file = os.path.join(directory_path, f'{date}.json')

    news = get_news(name, date) # get all news for specific date
    if news:
        save_data_json(output_json_file, news) # save output to json
        print(f'Data for date: {date} safed in folder {name}')
        print(f"Full path to file with news: {output_json_file}")



if __name__ == '__main__':
    company_dates = [(path, date) for path in full_path_list for date in get_dates(path)]

    # Use multiprocessing to parallelize the process
    with Pool(processes=4) as pool:  # Adjust the number of processes as needed
        pool.map(process_company_date, company_dates)
