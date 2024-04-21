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


@app.route('/c/<text>')
def Capturing(text):
    """
    A function to capture the text
    """
    return "C " + text


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
