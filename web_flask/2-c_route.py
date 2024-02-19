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


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
