#!/usr/bin/python3
"""
script that starts a Flask web application
"""

from flask import Flask

app = Flask(__name__)
host = "0.0.0.0"
port = 5000


@app.route("/", strict_slashes=False)
def HelloHBNB():
    """This function will be executed
    when the root URL (“/”) is accessed.

    Returns:
        str: returns a simple greeting.
    """
    return "Hello HBNB!"


@app.route("/hbhb", strict_slashes=False)
def HBHB():
    """This function will be executed
    when the root URL (“/hbhb”) is accessed.

    Returns:
        str: returns a simple phrase.
    """
    return "HBNB"


if __name__ == "__main__":
    app.run(host, port)