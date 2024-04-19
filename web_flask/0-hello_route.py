#!/usr/bin/python3
"""Flask framework
    """
from flask import Flask

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def greeting():
    return "Hello HBNB!"


if __name__ == "__main__":
    app.run()
