'''Counter App will count how many times the root page has been displayed
by Troy Center, Coding Dojo Python Flask fundamentals, using sessions'''

#pylint: disable=c0111,c0103
from flask import Flask, render_template, url_for, request, redirect, session

app = Flask(__name__)

app.secret_key = 'lkjas-0823lkasdasdasdas-478'

# increment the variable for the session counter.
# if it doesn't exit, create it. (first pass)
def sessionCounter():
    try:
        session['counter'] += 1
    except KeyError:
        session['counter'] = 1

@app.route('/')
def homepage():
    sessionCounter()
    return render_template('counter.html')
app.run(debug=True)