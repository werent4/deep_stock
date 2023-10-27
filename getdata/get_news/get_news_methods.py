import os
import glob
from gnews import GNews
from datetime import date, timedelta
import json
import csv

def save_data_json(output_json_file, news):
    '''Funct to save data to json file'''
    with open(output_json_file, 'w', encoding='utf-8') as json_file:
        json.dump(news, json_file, ensure_ascii=False, indent=4)

def get_list_companies(folder_path):
    '''
    Func to get list of full path to companies csv csv_files
    Returns array with full paths (array)
    '''
    csv_files = glob.glob(os.path.join(folder_path, '*.csv*'))
    return csv_files

def get_comp_name(path):
    '''
    Func to get comp name from path to its file
    Returns only name (str)
    '''

    name = os.path.splitext(os.path.basename(path))[0]
    return name

def get_dates(path_csv):
    '''
    Func to get list of dates from givet csv file
    Returns array
    '''

    with open(path_csv, newline='') as csvfile:
        reader = csv.DictReader(csvfile)

        # Extract the 'Date' column
        dates = [row['Date'] for row in reader]
        return dates

def get_news(comp_name, start_date):
    '''Func to get news for particular day
    return all news from that day(json array) or empty array'''
    end_date = start_date + timedelta(days=1)

    google_news = GNews(language='en', start_date= start_date, end_date= end_date,)

    raw_news = google_news.get_news(comp_name + ' stock')

    keys_to_keep = ['title', 'description', 'published date', 'url']

        # Create a new list with filtered information
    filtered_news = [{key: article[key] for key in keys_to_keep} for article in raw_news]
    return filtered_news
