import requests
from bs4 import BeautifulSoup
import sqlite3
import time

conn_1 = sqlite3.connect('r4r_pages.sqlite')
cur_1 = conn_1.cursor()

def spider_pages(x):
    # create first table
    cur_1.execute('CREATE TABLE IF NOT EXISTS pages_list (id INTEGER PRIMARY KEY AUTOINCREMENT, page_url BLOB, page_html BLOB)')

    start_url = x
    print("Spider initialized at ", start_url)
    # manually place first link and page html in db
    # target server will block requests from program without user agent details
    set_header = {'user-agent':'r4r-analysis'}
    get_start_url = requests.get(start_url, headers = set_header)
    # requests module fetches page as bytes so .text needed to convert to text
    soup = BeautifulSoup(get_start_url.text, 'html.parser')
    soup_text = str(soup.prettify())
    cur_1.execute('INSERT OR IGNORE INTO pages_list (page_url, page_html) VALUES (?, ?)', (start_url, soup_text, ))

    crawl_count = 10
    while crawl_count > 0:
        time.sleep(0.25)
        crawl_count = crawl_count -1
        get_start_url = requests.get(start_url, headers = set_header)
        soup = BeautifulSoup(get_start_url.text, 'html.parser')
        # download whole page html into soup_text
        soup_text = str(soup.prettify())
        span_tag = soup.find('span', class_='next-button')
        a_tag = span_tag.find('a')
        next_page = str(a_tag.attrs['href'])
        print(next_page)

        # place in db and loop again with new url
        cur_1.execute('INSERT OR IGNORE INTO pages_list (page_url, page_html) VALUES (?, ?)', (next_page, soup_text, ))
        start_url = next_page
    conn_1.commit()

def scrape_posts():
    # fetch downloaded pages from db
    pages = cur_1.execute('SELECT page_url, page_html FROM pages_list')
    for i in pages:
        page_url = i[0]
        page_html = i[1]
        soup = BeautifulSoup(page_html, 'html.parser')
        # structure is div : entry unvoted >>> a : title may-blank
        r4r_post_divs = soup.find_all('div', class_='entry unvoted')
        for x in r4r_post_divs:
            try:
                r4r_post_atag = x.find('a', class_='title may-blank ')
                post_url = str('https://www.reddit.com'+atag.attrs['href'])
                post_title_contents = str(atag.contents[0]).strip()
                time.sleep(1)
            except:
                print('Oops, cannot process <div>. Moving on...')


# spider_pages("https://www.reddit.com/r/r4r")
scrape_posts()
