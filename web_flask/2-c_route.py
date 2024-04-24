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


@app.route("/hbhb", strict_slashes=False)
def HBHB():
    """This function will be executed
    when the root URL (“/hbhb”) is accessed.
    """
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def C_text(text):
    """This function will be executed when
    the URL (“/c/<text>”) is accessed. The
    text provided in the URL is displayed
    after “C ”, with underscores replaced
    by spaces.
    """
    text = text.replace("_", " ")
    return "C {}".format(text)


if __name__ == "__main__":
    app.run(host, port)
