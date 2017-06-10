'''Counter App will count how many times the root page has been displayed
by Troy Center, Coding Dojo Python Flask fundamentals, using sessions'''

#pylint: disable=c0106,c0111

from flask import Flask, render_template, request, session

app=Flask(__name__)

@app.route('/')
def count_page_hits(): 
    print "homepage"
    pass

app.run(debug=True)