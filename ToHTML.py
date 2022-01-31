from flask import Flask
from flask import *
from functools import wraps
from flask import Flask, render_template, request
import cgi
import sqlite3

#class ToHTML:

app = Flask(__name__)

@app.route('/')
#def home():
#    title = 'Recipes'
#    return render_template('home.html', title = title)

@app.route('/res/')
def chooseInput():
    title = 'choose input'
    #form = cgi.FieldStorage()
    #restriction = form.getvalue('Please choose restriction number: 1 - Sugar-Free, 2 - Gluten-Free, 3 - Dairy-Free')
    #return restriction
    restriction = request.form.get("restriction")
    return render_template('home.html', title = title, restriction = restriction)

    #@app.route('/hi/')
    #def who(self):
     #   return "Who are you?"

    #@app.route('/hi/<username>')
    #def greet(self, username):
     #   return f"Hi there, {username}!"

if __name__ == '__main__':
    app.run()