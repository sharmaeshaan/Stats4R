import sqlite3
import time
import statistics
from decimal import Decimal

conn = sqlite3.connect('r4r_posts_breakdown.sqlite')
cur = conn.cursor()

# start and end date of posts to be analysed 
def dates():
    # get the post_date column order it as ascending and get the first record
    cur.execute('SELECT post_date FROM posts_breakdown ORDER BY post_date ASC LIMIT 1')
    # cur.fetchall() gets a tuple inside a list
    start_date = cur.fetchall()[0][0]
    cur.execute('SELECT post_date FROM posts_breakdown ORDER BY post_date DESC LIMIT 1')
    end_date = cur.fetchall()[0][0]
    return {'start date':start_date, 'end date':end_date}

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

# total no. of trans
def total_trans():
    cur.execute('SELECT * FROM posts_breakdown WHERE sex=?', ('t', ))
    trans = cur.fetchall()
    return len(trans)

# no. of males seeking females
def m4f():
    cur.execute('SELECT * FROM posts_breakdown WHERE sex = ? AND seeking = ?', ('m', 'f', ))
    m4f = cur.fetchall()
    return len(m4f)

# no. of males seeking males
def m4m():
    cur.execute('SELECT * FROM posts_breakdown WHERE sex = ? AND seeking = ?', ('m', 'm', ))
    m4m = cur.fetchall()
    return len(m4m)

# no. of males seeking redditors
def m4r():
    cur.execute('SELECT * FROM posts_breakdown WHERE sex=? AND seeking = ?', ('m', 'r', ))
    m4r = cur.fetchall()
    return len(m4r)

# no. of females seeking males
def f4m():
    cur.execute('SELECT * FROM posts_breakdown WHERE sex = ? AND seeking = ?', ('f', 'm', ))
    f4m = cur.fetchall()
    return len(f4m)

# no. of females seeking females
def f4f():
    cur.execute('SELECT * FROM posts_breakdown WHERE sex = ? AND seeking = ?', ('f', 'f', ))
    f4f = cur.fetchall()
    return len(f4f)

# no. of females seeking redditors
def f4r():
    cur.execute('SELECT * FROM posts_breakdown WHERE sex=? AND seeking = ?', ('f', 'r', ))
    f4r = cur.fetchall()
    return len(f4r)

# average number of upvotes on posts by males
def maleupvotes():
    upvotes = cur.execute('SELECT final_upvotes FROM posts_breakdown WHERE sex = ?', ('m',))
    upvotes_list = list()
    for i in upvotes:
        upvotes_list.append(i[0])
    mean_upvotes = statistics.mean(upvotes_list)
    # round off the average score upto 2 decimal points
    rounded = round(mean_upvotes, 2)
    return rounded

# average number of upvotes on posts by females
def femaleupvotes():
    upvotes = cur.execute('SELECT final_upvotes FROM posts_breakdown WHERE sex = ?', ('f',))
    upvotes_list = list()
    for i in upvotes:
        upvotes_list.append(i[0])
    mean_upvotes = statistics.mean(upvotes_list)
    rounded = round(mean_upvotes, 2)
    return rounded

# average number of comments on posts by males
def malecomments():
    comments = cur.execute('SELECT comments_number FROM posts_breakdown WHERE sex = ?', ('m',))
    comments_list = list()
    for i in comments:
        comments_list.append(i[0])
    mean_comments = statistics.mean(comments_list)
    rounded = round(mean_comments, 2)
    return rounded

# average number of comments on posts by females
def femalecomments():
    comments = cur.execute('SELECT comments_number FROM posts_breakdown WHERE sex = ?', ('f',))
    comments_list = list()
    for i in comments:
        comments_list.append(i[0])
    mean_comments = statistics.mean(comments_list)
    rounded = round(mean_comments, 2)
    return rounded

# print('Total men: ', total_males())
# print('Total women: ', total_females())
# print('Average age: ', mean_age())
# print('Average age of women: ', mean_age_f())
# print('Average age of men: ', mean_age_m())
# print('Men seeking women: ', m4f())
# print('Women seeking men: ', f4m())
# print('Men seeking men: ', m4m())
# print('Women seeking women: ', f4f())
# print('Average upvotes score of posts by males: ', maleupvotes())
# print('Average upvotes score of posts by females: ', femaleupvotes())
# print('Average number of comments on posts by males: ', malecomments())
# print('Average number of comments on posts by males: ', femalecomments())
# print('Start date and End date: ', dates())