#!/usr/bin/python3
"""Framework for Flask"""
from flask import Flask

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_world():
    """Returns hello hbhb"""
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def HBNB():
    """Returns HBNB"""
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def text(text):
    """Returns the text given"""
    return "C {}".format(text.replace("_", " "))


if __name__ == "__main__":
    app.run()
