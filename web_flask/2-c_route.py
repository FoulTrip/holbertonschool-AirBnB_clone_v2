#!/usr/bin/python3

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


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """Displays 'HBNB'."""
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def c(text):
    """Displays 'C' followed by the value of <text>."""
    text = text.replace("_", " ")
    return "C {}".format(text)


if __name__ == "__main__":
    app.run(host, port)
