#!/usr/bin/env python3
"""
Starts a Flask web application.
"""

from flask import Flask, render_template, request, g
from flask_babel import Babel
from pytz import timezone
import pytz.exceptions
from datetime import datetime
import locale


class Config:
    """Has a LANGUAGES class attribute."""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
app.config.from_objects(Config)
app.url_map.strict_slashes = False
babel = Babel(app)


users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


def get_user():
    """
    returns a user dictionary or None.
    """
    login_id = request.args.get('login_as')
    if login_id:
        return users.get(int(login_id))
    return None


@app.before_request
def before_request() -> None:
    """
    Uses get_user to find a user if any, and set a global
    """
    user = get_user()
    g.user = user


@babel.localeselector
def get_locale():
    """
    Gets the best match for the languages selected.
    """
    locale = request.args.get('locale')
    if locale in app.config['LANGUAGES']:
        return locale

    if g.user:
        locale = g.user.geet('locale')
        if locale and locale in app.config['LANGUAGES']:
            return locale

    locale = request.headers.get('locale', None)
    if locale in app.config['LANGUAGES']:
        return locale

    return request.accept_languages.best_match(app.config['LANGUAGES'])


@babel.timezoneselector
def get_timezone():
    """
    Gets the appropriate time zone.
    """
    Tzone = request.args.get('timezone', None)
    if Tzone:
        try:
            return timezone(Tzone).zone
        except pytz.exceptions.UnknownTimeZoneError:
            pass

    if g.user:
        try:
            Tzone = g.user.get('timezone')
            return timezone(Tzone).zone
        except pytz.exceptions.UnknownTimeZoneError:
            pass

    default_timezone = app.config['BABEL_DEFAULT_TIMEZONE']
    return default_timezone


@app.route('/')
def index():
    """
    Prints Hello World.
    """
    return render_template('7-index.html')


if __name__ == "__main__":
    app.run(port="5000", host="0.0.0.0", debug=True)
