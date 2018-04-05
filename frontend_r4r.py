import sqlite3
from analyse_r4r import mean_age, total_males, total_females, m4f, m4m, f4f, f4m
from flask import Flask, render_template

app = Flask('testapp')

conn = sqlite3.connect('r4r_posts_breakdown.sqlite')
cur = conn.cursor()

meanage = mean_age()

@app.route('/')
def index():
    return render_template('index.html', meanage = meanage)

if __name__ == '__main__':
    app.run()