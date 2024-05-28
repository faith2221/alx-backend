#!/usr/bin/env python3
"""
Starts a Flask web application.
"""

from flask import Flask, render_template, request, g
from flask_babel import Babel


class Config:
    """Has a LANGUAGES class attribute."""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
app.config.from_objects(Config)
babel = Babel(app)


@app.route('/')
def index():
    """
    Prints Hello World.
    """
    return render_template('1-index.html')


if __name__ == "__main__":
    app.run(port="5000", host="0.0.0.0", debug=True)
