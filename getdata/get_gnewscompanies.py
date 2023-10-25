from methods import read_data_pickle
from multiprocessing import Pool
from gnews import GNews
import pickle
import json
import time

#path_comps - path to the picke file with comp names
def get_comp_names(path_comps):
    data = read_data_pickle(path_comps)
    # Get the comp names
    companies = [item[0] for item in data]

    return companies

def save_news(comp, save_path):
    google_news = GNews()
    #for comp in list_of_comp_names:
    print(comp + ' stock data:')
    news = google_news.get_news(comp + ' stock')

    output_json_file = f'{save_path}\{comp}.json'
    with open(output_json_file, 'w', encoding='utf-8') as json_file:
            json.dump(news[:10], json_file, ensure_ascii=False, indent=4)

    print(f'saved to {output_json_file}')
    time.sleep(5)

if __name__ == '__main__':
    #!important
    # need adjustment for ur own
    path_comps = r'com_names\009_min_fall_60d_13_10_2023.pickle'
    save_path = r'C:\Users\werent4\Desktop\deep_stock\datasets\comp_news'

    companies = get_comp_names(path_comps)

    # Create a pool of worker processes
    #!important
    pool = Pool(processes=4)# need adjustment for ur own based on cores of CPU

    # Use the pool to parallelize the news fetching for companies
    pool.starmap(save_news, [(comp, save_path) for comp in companies[223:]])

    pool.close()
    pool.join()
