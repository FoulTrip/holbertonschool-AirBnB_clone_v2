#!/usr/bin/python3

from flask import Flask

app = Flask(__name__)
host = "0.0.0.0"
port = 5000


@app.route("/", strict_slashes=False)
def HelloHBNB():
    return "Hello HBNB!"


@app.route("/hbhb", strict_slashes=False)
def HBHB():
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def C_text(text):
    text = text.replace("_", " ")
    return f"C {text}"


if __name__ == "__main__":
    app.run(host, port)
