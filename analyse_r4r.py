import sqlite3
import time
import statistics

conn = sqlite3.connect('r4r_posts_breakdown.sqlite')
cur = conn.cursor()

# average age
def mean_age():
    ages_tuple = cur.execute('SELECT age FROM posts_breakdown')
    ages_list = list()
    for i in ages_tuple:
        ages_list.append(i[0])
    mean = int(statistics.mean(ages_list))
    return mean

# average age of females
def mean_age_f():
    f_ages = cur.execute('SELECT age FROM posts_breakdown WHERE sex="f";')
    ages_list = list()
    for i in f_ages:
        ages_list.append(i[0])
    mean_f = int(statistics.mean(ages_list))
    return mean_f

# average age of females
def mean_age_m():
    m_ages = cur.execute('SELECT age FROM posts_breakdown WHERE sex="m";')
    ages_list = list()
    for i in m_ages:
        ages_list.append(i[0])
    mean_m = int(statistics.mean(ages_list))
    return mean_m

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

print('Average age: ', mean_age())
print('Average age of women: ', mean_age_f())
print('Average age of men: ', mean_age_m())
print('Men seeking women: ', m4f())
print('Women seeking men: ', f4m())
print('Total men: ', total_males())
print('Total women: ', total_females())
print('Men seeking men: ', m4m())
print('Women seeking women: ', f4f())