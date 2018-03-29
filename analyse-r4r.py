import requests
from bs4 import BeautifulSoup
import sqlite3

def spider_pages(x):
    start_url = x
    print("Spider initialized at ", start_url)

    # target server will block requests from program without user agent details
    set_header = {'user-agent':'r4r-data-analysis'}
    get_start_url = requests.get(start_url, headers = set_header)

    # requests module fetches page as bytes so .text needed to convert to text
    soup = BeautifulSoup(get_start_url.text, 'html.parser')
    span_tag = soup.find('span', class_='next-button')
    a_tag = span_tag.find('a')
    next_button = str(a_tag.attrs['href'])
