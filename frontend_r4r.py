import sqlite3
from analyse_r4r import mean_age, total_males, total_females, m4f, m4m, f4f, f4m
import matplotlib.pyplot as plt


conn = sqlite3.connect('r4r_posts_breakdown.sqlite')
cur = conn.cursor()


def m2f():
    labels = 'Males', 'Females'
    sizes = [total_males(), total_females()]

    fig1, ax1 = plt.subplots()

    ax1.pie(sizes, labels=labels, startangle=90, autopct='%1.1f%%')
    ax1.axis('equal')

    plt.show()

def seeking():
    seeking = {'Males\nseeking\nFemales':m4f(), 'Females\nseeking\nMales':f4m(), 'Males\nseeking\nMales':m4m(), 'Females\nseeking\nFemales':f4f()}
    names = list(seeking.keys())
    values = list(seeking.values())

    plt.subplot(121)
    plt.bar(range(len(seeking)), values, tick_label = names, align='center')
    # plt.xticks(rotation='75')
    # plt.subplots_adjust(bottom=0.3)
    plt.show()

seeking()