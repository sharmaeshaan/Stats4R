import sqlite3
import time

conn = sqlite3.connect('r4r_posts_breakdown.sqlite')
cur = conn.cursor()

def sanitise():
    cur.execute('DELETE FROM posts_breakdown WHERE seeking != ? AND seeking != ? AND seeking!= ? AND seeking!= ?', ('m', 'f', 'r', 't', ))
    cur.execute('DELETE FROM posts_breakdown WHERE sex != ? AND sex != ? AND sex!= ? AND sex!= ?', ('m', 'f', 'r', 't', ))
    conn.commit()

sanitise()
