#!/usr/bin/python3
"""Framework for Flask"""
from flask import Flask

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def greeting():
    """Returns hbhb greeting"""
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """Returns HBNB"""
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def echo(text):
    """Returns the text given"""
    return "C {}".format(text.replace("_", " "))


if __name__ == "__main__":
    app.run()
