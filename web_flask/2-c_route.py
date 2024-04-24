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

    Returns:
        str: returns a simple phrase.
    """
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def C_text(text):
    """This function will be executed when
    the URL (“/c/<text>”) is accessed. The
    text provided in the URL is displayed
    after “C ”, with underscores replaced
    by spaces.

    args:
        text (str): The text provided in the URL

    Returns:
        str: Returns a string formatted with “C”
        followed by the text provided.
    """
    text = text.replace("_", " ")
    return f"C {text}"


if __name__ == "__main__":
    app.run(host, port)
