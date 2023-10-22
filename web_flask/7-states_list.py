#!/usr/bin/python3
"""This script starts Flask web application"""

from flask import Flask, render_template
from models import storage
from models.state import State

app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route("/states_list")
def states_list():
    """
    /states_list: displays html page
    H1 tag: “States”
    UL tag: with the list of all State objects present in DBStorage
    """
    states = [s for s in storage.all("State").values()]
    return render_template("7-states_list.html", states=states)


@app.teardown_appcontext
def tear_down(self):
    """Remove current SQLAlchemy session, after each request"""
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
