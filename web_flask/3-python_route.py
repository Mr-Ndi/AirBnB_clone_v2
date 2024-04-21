#!/usr/bin/python3
""" Starting a Flask web application """

from flask import Flask


app = Flask(__name__)


@app.route('/', strict_slashes=False)
def Say_hello():
    """
    A function to print hello to Mr HBNB
    """
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def Displaying():
    """
    A fuction to show hbnb on hbnb
    """
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def Capturing(text):
    """
    A function to capture the text that follows c
    """
    text = text.replace('_', ' ')
    return "C {}".format(text)


@app.route('/python/', defaults={'text': 'is cool'}, strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def Capturing_for_python(text):
    """
    A function to capture the text that follows python
    """
    text = text.replace('_', ' ')
    return "Python {}".format(text)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
