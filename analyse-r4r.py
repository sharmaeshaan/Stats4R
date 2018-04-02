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
    return int(mean_age)

def m4f():
    cur.execute('SELECT * FROM posts_breakdown WHERE sex = ? and seeking = ?', ('m', 'f', ))
    m4f = cur.fetchall()
    return len(m4f)

def f4m():
    cur.execute('SELECT * FROM posts_breakdown WHERE sex = ? and seeking = ?', ('f', 'm', ))
    f4m = cur.fetchall()
    return len(f4m)

posts()
# sanitise()
print(mean_age())
print(m4f())
print(f4m())
