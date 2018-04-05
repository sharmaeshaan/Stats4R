import sqlite3
from analyse_r4r import mean_age_f, mean_age_m, total_males, total_females, m4f, m4m, f4f, f4m
import matplotlib.pyplot as plt


conn = sqlite3.connect('r4r_posts_breakdown.sqlite')
cur = conn.cursor()


def m2f():
    labels = 'Males', 'Females'
    sizes = [total_males(), total_females()]
    # create new figure and axis
    fig1, ax1 = plt.subplots()
    ax1.pie(sizes, labels=labels, startangle=90, autopct='%1.1f%%')
    ax1.axis('equal')

    plt.savefig('static/m2f.png', format='png')

def seeking():
    seeking = {'Males\nseeking\nFemales':m4f(), 'Females\nseeking\nMales':f4m(), 'Males\nseeking\nMales':m4m(), 'Females\nseeking\nFemales':f4f()}
    names = list(seeking.keys())
    values = list(seeking.values())
    # define plot size dimensions
    fig2, ax2 = plt.subplots()
    ax2.bar(range(len(seeking)), values, tick_label = names, align='center')
    # plt.xticks(rotation='75')
    # plt.subplots_adjust(bottom=0.3)
    plt.savefig('static/seeking.png', format='png')

def ages():
    ages = {'Males':mean_age_m(), 'Females':mean_age_f()}
    names2 = list(ages.keys())
    values2 = list(ages.values())
    # create new figure and axis
    fig3, ax3 = plt.subplots()
    # Get current axis (gca) of plot
    axes = plt.gca()
    # set 18-40 age range for y-axis
    axes.set_ylim([18, 35])
    # show horizontal grid lines
    axes.yaxis.grid(True)
    # set size of market with 's'
    ax3.scatter(names2, values2, s=200)
    # set label names
    plt.ylabel('Average Age')
    plt.savefig('static/ages.png', format='png')

m2f()
seeking()
ages()