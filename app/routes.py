from flask import Flask, render_template, request
from app import app

# Creating a Flask application object
app = Flask(__name__)

# Defining a route for the root URL '/'
@app.route('/')
def index():
    # Returning the template index.html
    return render_template('index.html')

# Defining a route for '/result'
@app.route('/result')
def result():
    # Returning the template result.html
    return render_template('result.html')

