from flask import Flask, render_template
from analyse_r4r import dates

startdate = dates().get('start date')
enddate = dates().get('end date')

app = Flask('stats4r')

@app.route('/')
def index():
    return render_template('index.html', startdate = startdate, enddate = enddate)

if __name__ == '__main__':
    app.run()