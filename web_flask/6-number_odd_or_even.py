#!/usr/bin/python3
"""Flask framework"""
from flask import Flask, url_for, render_template

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
    """Returns text given"""
    return "C {}".format(text.replace("_", " "))


@app.route('/python/', defaults={'text': 'is_cool'})
@app.route('/python/<text>', strict_slashes=False)
def echo_py(text):
    """Displays “Python ”, followed by the value of the text"""
    return "Python {}".format(text.replace("_", " "))


@app.route('/number/<int:n>', strict_slashes=False)
def display_int(n):
    """Displays “n is a number” only if n is an integer."""
    return "{} is a number".format(n)


@app.route('/number_template/<int:n>', strict_slashes=False)
def html_template(n):
    """Displays in HTML "n" is a number" only if n is an integer."""
    return render_template('5-number.html', name=n)


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def template_even_odd(n):
    """
        Displays in HTML "n is a number" only if n is an integer.
        H1 tag: Number: n is even|odd.
    """
    return render_template('6-number_odd_or_even.html', name=n)


if __name__ == "__main__":
    app.run()
