from gnews import GNews
import pickle
import json


#path_comps - path to the picke file with comp names
def get_comp_names(path_comps):
    # Open the .pickle file for reading in binary mode
    with open(path_comps, 'rb') as file:
        data = pickle.load(file)

    # Get the comp names
    companies = [item[0] for item in data]

    return companies

def save_news(list_of_comp_names, save_path):
    c = 1
    google_news = GNews()
    for comp in list_of_comp_names:
        print(comp + ' stock data:')
        news = google_news.get_news(comp + ' stock')

        output_json_file = f'{save_path}\{comp}.json'
        with open(output_json_file, 'w', encoding='utf-8') as json_file:
                json.dump(news[:10], json_file, ensure_ascii=False, indent=4)

        print(f'saved to {output_json_file}')
        c+=1
        if c == 10:
            break


path_comps = r'com_names\009_min_fall_60d_13_10_2023.pickle'
save_path = r'C:\Users\werent4\Desktop\deep_stock\datasets\comp_news'
companies = get_comp_names(path_comps)
save_news(companies, save_path)
