import requests
from bs4 import BeautifulSoup
import sqlite3

def spider_pages(x):
    start_url = x
    print("Spider initialized at ", start_url)

    set_header = {'user-agent':'r4r-data-analysis'}
