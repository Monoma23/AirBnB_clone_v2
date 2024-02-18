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

@app.route('/number/<n>', strict_slashes=False)
def nbr(n):
    """Displaying Hello HBNB!"""
    return "{:d} is a number".format(n)

@app.route('/number_template/<int:n>', strict_slashes=False)
def numbersn_templates(n):
    """Displaying a HTML page only if n is int"""
    return render_template('5-number.html', n=n)

@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def numbersn_evenness(n):
    """Display a HTML page only if n is integer"""
    if n % 2 == 0:
        evenness = 'even'
    else:
        evenness = 'odd'
    return render_template('6-number_odd_or_even.html', n=n,
                           evenness=evenness)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)