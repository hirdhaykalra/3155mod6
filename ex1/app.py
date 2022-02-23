#Worked with Haley Siharath
#Sources: https://www.geeksforgeeks.org/python-strftime-function/ --- used to get formatting string for strftime()
from flask import Flask, render_template, request
from datetime import datetime

app=Flask(__name__)

@app.route('/')
def index():
    _year = datetime.now()
    _year = _year.strftime("%A, %B %d %Y %X")
    return render_template('index.html', year = _year)