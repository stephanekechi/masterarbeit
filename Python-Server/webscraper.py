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
    
    def get_false_news(self):
        total_result = []

        for page_number in range(1, self.fake_scraping_page_nbr):
            request_string = 'https://www.politifact.com/factchecks/list/?page={nbr}&ruling=false'.format(nbr=page_number)
            false_request = requests.get(request_string)

            soup = BeautifulSoup(false_request.text, 'html.parser')
            results = soup.find_all('article', attrs={'class':'m-statement m-statement--is-medium m-statement--false'})

            records = []
            for result in results:
                subject_class =  result.find('div', attrs={'class':'m-statement__meta'})
                subject = subject_class.find('a', attrs={}).text
                text_class = result.find('div', attrs={'class': 'm-statement__quote'})
                text =  text_class.find('a', attrs={}).text
                #can be lately improve
                title = subject
                date_text = result.find('div', attrs={'class': 'm-statement__desc'}).text
                date = self.text_processor.retrieve_date(date_text)
                records.append((title, text, subject, date))
            
            total_result.extend(records)
        
        df = pd.DataFrame(total_result, columns=['title', 'text', 'subject', 'date'])
        #print(df.date)
        return df