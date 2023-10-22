#!/usr/bin/python3
"""This script starts Flask web application"""

from flask import Flask, render_template
from models import storage
from models.state import State

app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route("/states")
def states():
    """displays html page"""
    states = storage.all(State)
    return render_template("9-states.html", state=states, mode='all')


@app.route("/states/<id>")
def states_id(id):
    """displays html page"""
    for state in storage.all(State).values():
        if state.id == id:
            return render_template("9-states.html", state=state, mode='id')
        return render_template("9-states.html", state=state, mode='none')


@app.teardown_appcontext
def teardown(exception):
    """Remove current SQLAlchemy session, after each request"""
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
