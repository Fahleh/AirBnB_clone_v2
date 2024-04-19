#!/usr/bin/python3
"""Starts a Flask web application."""
from models import storage
from flask import Flask
from flask import render_template


app = Flask(__name__)


@app.teardown_appcontext
def cleanup(foo):
    """Closes session"""
    storage.close()


@app.route("/hbnb_filters", strict_slashes=False)
def hbnb_filters():
    """Displays the main HBnB filters HTML page."""
    states = storage.all("State")
    amenities = storage.all("Amenity")
    return render_template("10-hbnb_filters.html",
                           states=states, amenities=amenities)


if __name__ == "__main__":
    app.run(host="0.0.0.0")
