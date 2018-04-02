import sqlite3
import time
import statistics

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

def mean_age():
    ages = list()
    for i in posts():
        ages.append(i[3])
    mean_age = statistics.mean(ages)
    print(int(mean_age))


posts()
# sanitise()
mean_age()
