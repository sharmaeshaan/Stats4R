import sqlite3
import time

conn = sqlite3.connect('r4r_posts_breakdown.sqlite')
cur = conn.cursor()

def posts():
    posts_data = cur.execute('SELECT * FROM posts_breakdown')
    return posts_data

def sanitise():
    # delete entries where sex and seeking columns contain anything other than m, f, r or t
    cur.execute('DELETE FROM posts_breakdown WHERE seeking != ? AND seeking != ? AND seeking!= ? AND seeking!= ?', ('m', 'f', 'r', 't', ))
    cur.execute('DELETE FROM posts_breakdown WHERE sex != ? AND sex != ? AND sex!= ? AND sex!= ?', ('m', 'f', 'r', 't', ))
    # delete entries where age is not an integer
    cur.execute('DELETE FROM posts_breakdown WHERE age IS NULL')
    conn.commit()

def extract():
    posts_data = cur.execute('SELECT * FROM posts_breakdown')
    for i in posts_data:
        time.sleep(0.2)
        print(len(i[3]))

posts()
sanitise()
# extract()
# for i in posts():
#     # time.sleep(0.3)
#     print(i[3])
#     print('\n')
