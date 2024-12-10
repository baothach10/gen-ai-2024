import requests
from datetime import datetime
from dotenv import load_dotenv
import os
load_dotenv()

MEDIA_API_KEY = os.getenv('MEDIASTACK_KEY_NEW')
base_url = 'http://api.mediastack.com/v1/news'

class MediaStack:
    def __init__(self):
        self.api_key = MEDIA_API_KEY

    def get_news(self,keywords, date, language):
        params = {
            'access_key': self.api_key,
            'date': date,
            'languages': language,
            'keywords': keywords,
            'limit': 10
        }
        # print(params)
        response = requests.get(base_url, params=params)
        data = response.json()
        return data
    
    def get_titles(self, data):
        titles = []
        for article in data['data']:
            titles.append(article['title'])
        return titles
    
    def get_citations(self, data):
        citations = []
        for article in data['data']:
            citations.append(article['url'])
        return citations
    
    def get_descriptions(self, data):
        descriptions = []
        for article in data['data']:
            descriptions.append(article['description'])
        return descriptions


# mediaStack = MediaStack()
# print(mediaStack.get_news("crypto", datetime.today().strftime('%Y-%m-%d'), "en"))


   

    
