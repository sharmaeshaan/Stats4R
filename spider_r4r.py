import requests
from bs4 import BeautifulSoup
import sqlite3
import time

# setup databases
conn_1 = sqlite3.connect('r4r_pages.sqlite')
cur_1 = conn_1.cursor()
conn_2 = sqlite3.connect('r4r_posts.sqlite')
cur_2 = conn_2.cursor()
conn_3 = sqlite3.connect('r4r_posts_breakdown.sqlite')
cur_3 = conn_3.cursor()

#set header for spider requests
set_header = {'user-agent':'r4r-analysis'}

def spider_pages(x):
    # create first table
    cur_1.execute('CREATE TABLE IF NOT EXISTS pages_list (id INTEGER PRIMARY KEY AUTOINCREMENT, page_url BLOB, page_html BLOB)')
    start_url = x
    print("Spider initialized at ", start_url)
    # manually place first link and page html in db
    # target server will block requests from program without user agent details
    get_start_url = requests.get(start_url, headers = set_header)
    # requests module fetches page as bytes so .text needed to convert to text
    soup = BeautifulSoup(get_start_url.text, 'html.parser')
    soup_text = str(soup.prettify())
    cur_1.execute('INSERT OR IGNORE INTO pages_list (page_url, page_html) VALUES (?, ?)', (start_url, soup_text, ))

    # r4r makes 26 pages available max
    count = 26
    while count > 0:
        count = count - 1
        try:
            time.sleep(0.10)
            get_start_url = requests.get(start_url, headers = set_header)
            soup = BeautifulSoup(get_start_url.text, 'html.parser')
            # download whole page html into soup_text
            soup_text = str(soup.prettify())
            span_tag = soup.find('span', class_='next-button')
            # break loop if spider reaches page with no 'next' button
            if str(span_tag) == None:
                break
            else:
                a_tag = span_tag.find('a')
                next_page = str(a_tag.attrs['href'])
                print(next_page)
                print('Spidering onwards...')
                # place in db and loop again with new url
                cur_1.execute('INSERT OR IGNORE INTO pages_list (page_url, page_html) VALUES (?, ?)', (next_page, soup_text, ))
                conn_1.commit()
                start_url = next_page
        except:
            print('Error')
    print('Spidering pages complete')

def scrape_posts():
    # create second table
    cur_2.execute('CREATE TABLE IF NOT EXISTS posts_list (id INTEGER PRIMARY KEY AUTOINCREMENT, post_url BLOB, post_title BLOB UNIQUE, post_html BLOB)')
    # fetch downloaded pages from first db
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
                # extract posts url and title content
                post_url = str('https://www.reddit.com'+r4r_post_atag.attrs['href'])
                post_title_contents = str(r4r_post_atag.contents[0]).strip()
                print('Scraping: ', post_url)
                print(post_title_contents)
                # time.sleep(1)
                # extract html of each individual post page
                try:
                    post_page = requests.get(post_url, headers=set_header)
                    post_page_html = str(post_page.text)
                except:
                    print('***Cannot fetch post page html. Oh well, moving on...***')
                # table inserts inside 'try/except' since unique constraint on post title can glitch
                try:
                    cur_2.execute('''
                    INSERT OR IGNORE INTO posts_list (post_url, post_title, post_html) VALUES (?, ?, ?)
                    ''', (post_url, post_title_contents, post_page_html))
                except:
                    print('***Cannot insert in DB. Oh well, moving on...***')
            except:
                print('***Oops, cannot process <div>, moving on...***')
        conn_2.commit()
        print('--Inserted--')

def breakdown_posts():
    # create third table
    cur_3.execute('CREATE TABLE IF NOT EXISTS posts_breakdown (id INTEGER PRIMARY KEY AUTOINCREMENT, post_url BLOB, post_date BLOB, comments_number INT, final_upvotes INT, post_title BLOB, age INTEGER, location BLOB, sex BLOB, seeking BLOB)')
    # fetch posts from second table
    posts = cur_2.execute('SELECT post_url, post_title, post_html FROM posts_list')
    for i in posts:
        post_url = i[0]
        post_page_html = i[2]
        post_title = i[1]
        post_title_split = post_title.split(' ')
        # if age is int then enter else enter null/none
        try:
            age = int(post_title_split[0])
        except:
            age = None
        try:
            category = post_title_split[1].lower()
            location = post_title_split[2]
        except:
            print('Error processing post title:', post_title)
            pass
        try:
            category_split = list(category)
            sex = category_split[1]
            seeking = category_split[3]
        except:
            print('Error processing post category: ', post_title)
            pass
        post_page_soup = BeautifulSoup(post_page_html, 'html.parser')
        try:
            pageinfo = post_page_soup.find('div', class_='linkinfo')
        except:
            print('Could not get page info')
            pass
        try:
            post_timestamp_block = pageinfo.find('div', class_='date')
            post_timestamp = post_timestamp_block.find('time')
            post_date = str(post_timestamp.contents[0])
        except:
            print('Could not process timestamp')
            pass
        try:
            post_score = pageinfo.find('div', class_='score')
            post_upvote_number = post_score.find('span', class_='number')
            post_final_upvote = int(post_upvote_number.contents[0])
        except:
            print('Could not process upvote count')
        try:
            post_commentarea = post_page_soup.find('div', class_='commentarea')
            commentarea_titlearea = post_commentarea.find('div', class_='panestack-title')
            comment_title = commentarea_titlearea.find('span', class_='title')
            comment_number_text = comment_title.contents[0]
            if comment_number_text == "no comments (yet)":
                comment_number = 0
            else:
                comment_number_text_list = comment_number_text.split(' ')
                comment_number = comment_number_text_list[1]
        except:
            print('Could not process comment number')
            pass
        # print(post_title)
        # print(age)
        # print(sex)
        # print(seeking)
        # print(post_date)
        # print(post_final_upvote)
        # print(comment_number)
        # print('\n')
        cur_3.execute('INSERT OR IGNORE INTO posts_breakdown (post_url, post_title, age, location, sex, seeking, comments_number,final_upvotes, post_date) VALUES (?,?,?,?,?,?,?,?,?)', (post_url, post_title, age, location, sex, seeking, comment_number, post_final_upvote, post_date))
    conn_3.commit()
    print('--Inserted--')

def sanitise():
    # delete entries where sex and seeking columns contain anything other than m, f, r or t
    cur_3.execute('DELETE FROM posts_breakdown WHERE seeking != ? AND seeking != ? AND seeking!= ? AND seeking!= ?', ('m', 'f', 'r', 't', ))
    cur_3.execute('DELETE FROM posts_breakdown WHERE sex != ? AND sex != ? AND sex!= ? AND sex!= ?', ('m', 'f', 'r', 't', ))
    # delete entries where age is not an integer
    cur_3.execute('DELETE FROM posts_breakdown WHERE age IS NULL')
    conn_3.commit()
    print('Sanitized')

spider_pages('https://www.reddit.com/r/r4r')
scrape_posts()
breakdown_posts()
sanitise()