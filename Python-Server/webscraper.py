import requests 
import pandas as pd
from bs4 import BeautifulSoup
import datefinder
from textprocessor import Textprocessor

class WebScraper:

    true_scraping_page_nbr = 0
    fake_scraping_page_nbr = 0
    text_processor = None

    def __init__(self, true_scraping_page_nbr, fake_scraping_page_nbr):
        self.true_scraping_page_nbr = true_scraping_page_nbr
        self.fake_scraping_page_nbr = fake_scraping_page_nbr
        self.text_processor = Textprocessor('TextProcessor')
    
    def process_soup_results(self, soup_result):
        result_array = []
        for result in soup_result:
            date_text = result.find('div', attrs={'class': 'm-statement__desc'}).text
            date = self.text_processor.retrieve_date(date_text)
            subject_class =  result.find('div', attrs={'class':'m-statement__meta'})
            subject = subject_class.find('a', attrs={}).text
            text_class = result.find('div', attrs={'class': 'm-statement__quote'})
            text =  text_class.find('a', attrs={}).text + ' ' + str(date)
            #can be lately improve
            title = subject
            result_array.append((title, text, subject, date))
        
        return result_array

    def process_news(self, process_obj):
        process_result = []
        for page_number in range(1, process_obj['range']):
            request_string = 'https://www.politifact.com/factchecks/list/?page={nbr}&ruling={ruling}' \
            .format(nbr=page_number, ruling=process_obj['ruling'])

            request = requests.get(request_string)
            soup = BeautifulSoup(request.text, 'html.parser')
            article_str_class = 'm-statement m-statement--is-medium m-statement--{ruling}' \
            .format(ruling=process_obj['ruling'])

            results = soup.find_all('article', attrs={'class':article_str_class})
            records = self.process_soup_results(results)
            process_result.extend(records)

        return process_result
        
        df = pd.DataFrame(total_result, columns=['title', 'text', 'subject', 'date'])
        return df        

    def get_false_news(self):
        process_obj = {
            'range': self.fake_scraping_page_nbr,
            'ruling': 'false'
        }
        total_result = self.process_news(process_obj)

        df = pd.DataFrame(total_result, columns=['title', 'text', 'subject', 'date'])
        return df

    def get_true_news(self):
        total_result = []
        process_obj_most_true = {
            'range': self.true_scraping_page_nbr,
            'ruling': 'mostly-true'
        }
        mst_true_temp_result = self.process_news(process_obj_most_true)
        total_result.extend(mst_true_temp_result)

        process_obj_true = {
            'range': self.true_scraping_page_nbr,
            'ruling': 'true'
        }
        true_temp_result = self.process_news(process_obj_true)
        total_result.extend(true_temp_result)
       
        df = pd.DataFrame(total_result, columns=['title', 'text', 'subject', 'date'])
        return df