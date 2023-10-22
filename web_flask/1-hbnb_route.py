#!/usr/bin/python3
"""This script starts Flask web application"""

from flask import Flask

app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route("/")
def hello():
    """/: displays (Hello HBNB!)"""
    return "Hello HBNB!"


@app.route("/hbnb")
def hbnb():
    '''/hbnb: displays (HBNB)'''
    return "HBNB"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
