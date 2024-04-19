#!/usr/bin/python3
"""Flask framework
"""
from flask import Flask

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def greeting():
    """return hello hbhb"""
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """Returns HBNB"""
    return "HBNB"


if __name__ == "__main__":
    app.run()
