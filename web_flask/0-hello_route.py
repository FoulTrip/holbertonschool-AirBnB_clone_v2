#!/usr/bin/python3

from flask import Flask

app = Flask(__name__)
host = "0.0.0.0"
port = 5000


@app.route("/", strict_slashes=False)
def HelloHBNB():
    return "Hello HBNB!"


if __name__ == "__main__":
    app.run(host, port)
