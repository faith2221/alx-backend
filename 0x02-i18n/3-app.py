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


@babel.localeselector
def get_locale():
    """
    Gets the best match for the languages selected.
    """
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/')
def index():
    """
    Prints Hello World.
    """
    return render_template('3-index.html')


if __name__ == "__main__":
    app.run(port="5000", host="0.0.0.0", debug=True)
