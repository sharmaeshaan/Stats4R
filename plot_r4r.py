import sqlite3
from analyse_r4r import mean_age_f, mean_age_m, total_males, total_females, total_trans, m4f, m4m, f4f, f4m, m4r, f4r, maleupvotes, femaleupvotes, malecomments, femalecomments
import matplotlib.pyplot as plt

conn = sqlite3.connect('r4r_posts_breakdown.sqlite')
cur = conn.cursor()

def population():
    labels = 'Males', 'Females', 'Trans'
    sizes = [total_males(), total_females(), total_trans()]
    # create new figure and axis
    fig1, ax1 = plt.subplots()
    ax1.pie(sizes, labels=labels, startangle=90, autopct='%1.1f%%')
    ax1.axis('equal')

    plt.savefig('static/population.svg', format='svg', transparent=True)

def seeking():
    seeking = {'Males\nseeking\nFemales':m4f(), 'Females\nseeking\nMales':f4m(), 'Males\nseeking\nMales':m4m(), 'Females\nseeking\nFemales':f4f(), 'Males\nseeking\nRedditors':m4r(), 'Females\nseeking\nRedditors':f4r()}
    names = list(seeking.keys())
    values = list(seeking.values())
    # define plot size dimensions
    fig2, ax2 = plt.subplots(figsize=(20, 10))
    ax2.bar(range(len(seeking)), values, tick_label = names, align='center', color='#b8a0ff')
    # plt.xticks(rotation='75')
    plt.xticks(fontsize=19)
    plt.yticks(fontsize=17)
    plt.savefig('static/seeking.svg', format='svg', transparent=True)

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
    ax3.scatter(names2, values2, s=200, color='#ff6f71')
    # set label names
    plt.ylabel('Average Age')
    plt.savefig('static/ages.svg', format='svg', transparent=True)

def upvotes():
    mean_upvotes = {'Upvotes\nto\nMales':maleupvotes(), 'Upvotes\nto\nFemales':femaleupvotes()}
    names = list(mean_upvotes.keys())
    values = list(mean_upvotes.values())
    # define plot size dimensions
    fig2, ax2 = plt.subplots()
    ax2.bar(range(len(mean_upvotes)), values, tick_label = names, align='center', color='#ffba2f')
    # plt.xticks(rotation='75')
    plt.savefig('static/upvotes.svg', format='svg', transparent=True)

def comments():
    mean_comments = {'Comments\nto\nMales':malecomments(), 'Comments\nto\nFemales':femalecomments()}
    names = list(mean_comments.keys())
    values = list(mean_comments.values())
    # define plot size dimensions
    fig2, ax2 = plt.subplots()
    ax2.bar(range(len(mean_comments)), values, tick_label = names, align='center', color='#a880ff')
    # plt.xticks(rotation='75')
    plt.savefig('static/comments.svg', format='svg', transparent=True)

population()
seeking()
ages()
upvotes()
comments()