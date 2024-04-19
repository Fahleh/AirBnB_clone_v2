#!/usr/bin/python3
"""Framework of Flask"""
from flask import Flask

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def greeting():
    """Returns hello hbhb"""
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """Returns HBNB"""
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def echo(text):
    """Returns the text given"""
    return "C {}".format(text.replace("_", " "))


@app.route('/python/', defaults={'text': 'is_cool'})
@app.route('/python/<text>', strict_slashes=False)
def echo_py(text):
    """Displays “Python ”, followed by the value of the text"""
    return "Python {}".format(text.replace("_", " "))


@app.route('/number/<int:n>', strict_slashes=False)
def display_int(n):
    """Displays “n is a number” only"""
    return "{} is a number".format(n)

if __name__ == "__main__":
    app.run()
