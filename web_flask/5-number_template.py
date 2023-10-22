#!/usr/bin/python3
"""This script starts Flask web application"""

from flask import Flask, render_template

app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route("/")
def hello():
    """/: displays (Hello HBNB!)"""
    return "Hello HBNB!"


@app.route("/hbnb")
def hbnb():
    """/hbnb: displays (HBNB)"""
    return "HBNB"


@app.route("/c/<text>")
def C_text(text):
    """/c/<text>: displays C followed by the text variable"""
    return "C {}".format(text.replace('_', ' '))


@app.route('/python')
@app.route('/python/<text>')
def python_text(text="is cool"):
    """
    /python/<text>: displays Python followed by the text variable
    """
    return "Python {}".format(text.replace('_', ' '))


@app.route("/number/<int:n>")
def text_int(n):
    """/number/<n>: displays (n is a number) only if integer"""
    return "{} is a number".format(n)


@app.route('/number_template/<int:n>')
def html_int(n):
    """/number_template/<n>: displays html page only if integer"""
    return render_template('5-number.html', n=n)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
