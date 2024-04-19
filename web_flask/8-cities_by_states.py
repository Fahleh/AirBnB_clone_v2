#!/usr/bin/python3
"""Starts a Flask web application."""
from models import storage
from flask import Flask
from flask import render_template


app = Flask(__name__)


@app.teardown_appcontext
def cleanup(foo):
    """Removes the current SQLAlchemy session."""
    storage.close()


@app.route('/cities_by_states', strict_slashes=False)
def states_list():
    """lists states from storage engine"""
    states = list(storage.all(State).values())
    return render_template('8-cities_by_states.html', states=states)


if __name__ == "__main__":
    app.run(host="0.0.0.0")
