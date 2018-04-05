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

def m4f_f4m():
    names = ['m4f', 'f4m']
    values = [m4f(), f4m()]
    plt.subplot(131)
    plt.bar(names, values)
    plt.show()