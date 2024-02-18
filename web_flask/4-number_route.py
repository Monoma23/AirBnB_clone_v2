#!/usr/bin/python3
"""Startingg Flask web app"""
from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """Displaying Hello HBNB!"""
    return "Hello HBNB!"

@app.route('/hbnb', strict_slashes=False)
def only_hbnb():
    """Displaying Hello HBNB!"""
    return "HBNB"

@app.route('/c/<text>', strict_slashes=False)
def C_isfun(text):
    """Displaying Hello HBNB!"""
    return "C" + text.replace('_', ' ')

@app.route('/python/<text>', strict_slashes=False)
def py_iscool(text='is cool'):
    """Displaying Hello HBNB!"""
    return "Python" + text.replace('_', ' ')

@app.route('/number/<int:n>', strict_slashes=False)
def nbr(n):
    """Displaying Hello HBNB!"""
    return "{:d} is a number".format(n)

@app.route('/number_template/<int:n>', strict_slashes=False)
def numbersntemplates(n):
    """Display a HTML page if n is int"""
    return render_template('5-number.html', n=n)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)