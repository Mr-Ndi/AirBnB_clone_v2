#!/usr/bin/python3
""" Starting a Flask web application """

from flask import Flask


app = Flask(__name__)


@app.route('/', strict_slashes=False)
def Say_hello():
    ''' A function to print hello to Mr HBNB'''
    return 'Hello HBNB!'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
