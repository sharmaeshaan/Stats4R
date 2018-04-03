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

# average age
def mean_age():
    ages = list()
    for i in posts():
        ages.append(i[3])
    mean_age = statistics.mean(ages)
    return int(mean_age)

# total no. of males
def total_males():
    cur.execute('SELECT * FROM posts_breakdown WHERE sex = ?', ('m', ))
    males = cur.fetchall()
    return len(males)

# total no. of females
def total_females():
    cur.execute('SELECT * FROM posts_breakdown WHERE sex = ?', ('f', ))
    females = cur.fetchall()
    return len(females)

# no. of males seeking females
def m4f():
    cur.execute('SELECT * FROM posts_breakdown WHERE sex = ? and seeking = ?', ('m', 'f', ))
    m4f = cur.fetchall()
    return len(m4f)

# no. of males seeking males
def m4m():
    cur.execute('SELECT * FROM posts_breakdown WHERE sex = ? and seeking = ?', ('m', 'm', ))
    m4m = cur.fetchall()
    return len(m4m)

# no. of females seeking males
def f4m():
    cur.execute('SELECT * FROM posts_breakdown WHERE sex = ? and seeking = ?', ('f', 'm', ))
    f4m = cur.fetchall()
    return len(f4m)

# no. of females seeking females
def f4f():
    cur.execute('SELECT * FROM posts_breakdown WHERE sex = ? and seeking = ?', ('f', 'f', ))
    f4f = cur.fetchall()
    return len(f4f)

# posts()
# # sanitise()
# print('Average age: ', mean_age())
# print('Men seeking women: ', m4f())
# print('Women seeking men: ', f4m())
# print('Total men: ', total_males())
# print('Total women: ', total_females())
# print('Men seeking men: ', m4m())
# print('Women seeking women: ', f4f())