import sqlite3
from analyse_r4r import mean_age_f, mean_age_m, total_males, total_females, m4f, m4m, f4f, f4m
import matplotlib.pyplot as plt


conn = sqlite3.connect('r4r_posts_breakdown.sqlite')
cur = conn.cursor()


def m2f_total():
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
    # define plot size dimensions
    plt.subplot(121)
    plt.bar(range(len(seeking)), values, tick_label = names, align='center')
    # plt.xticks(rotation='75')
    # plt.subplots_adjust(bottom=0.3)
    plt.show()

def m2f_ages():
    ages = {'Average Age Males':mean_age_m(), 'Average Age Females':mean_age_f()}
    names = list(ages.keys())
    values = list(ages.values())
    # define plot size dimensions
    plt.subplot(121)
    # Get current axis (gca) of plot
    axes = plt.gca()
    # set 18-40 age range for y-axis
    axes.set_ylim([18, 35])
    # show horizontal grid lines
    axes.yaxis.grid(True)
    # set size of market with 's'
    plt.scatter(names, values, s=200)
    plt.show()

m2f_ages()