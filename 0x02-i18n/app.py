#!/usr/bin/env python3
"""
Basic Flask app
"""
from datetime import datetime
from flask import Flask, render_template, request, g
from flask_babel import Babel, _, format_datetime
from typing import Union, Optional
from os import getenv
from pytz import timezone
import pytz.exceptions

users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


class Config():
    '''class that defines languages'''
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'

app = Flask(__name__)

app.config.from_object(Config)

def get_locale():
    """Sets the config class to the app"""
    if request.args.get('locale'):
        locale = request.args.get('locale')
        if locale in app.config['LANGUAGES']:
            return locale
    elif g.user and g.user.get('locale')\
        and g.user.get('locale') in app.config['LANGUAGES']:
        return g.user.get('locale')
    else:
        return request.accept_languages.best_match(app.config['LANGUAGES'])

@app.route('/')
def index():
    """ the default route for the application """
    timezone = get_timezone()
    tz = pytz.timezone(timezone)
    current_time = datetime.now(tz)
    current_time = format_datetime(datetime=current_time)
    return render_template("index.html", current_time=current_time)

@app.before_request
def before_request():
    """ finds user and sets as global on flask.g.user """
    g.user = get_user()
    g.time = get_timezone()

def get_user() -> Union[dict, None]:
    """ returns user if ID can be found """
    login_as = request.args.get("login_as", False)
    if login_as:
        user = users.get(int(login_as), False)
        if user:
            return user
    return None

def get_timezone() -> Optional[str]:
    """ Determines best match for supported timezones """
    try:
        if request.args.get("timezone"):
            timezone = request.args.get("timezone")
            tz = pytz.timezone(timezone)

        elif g.user and g.user.get("timezone"):
            timezone = g.user.get("timezone")
            tz = pytz.timezone(timezone)
        else:
            timezone = app.config["BABEL_DEFAULT_TIMEZONE"]
            tz = pytz.timezone(timezone)

    except pytz.exceptions.UnknownTimeZoneError:
        timezone = "UTC"

    return timezone

babel = Babel(app, locale_selector=get_locale, timezone_selector=get_timezone)


if __name__ == '__main__':
    app.run(host="0.0.0.0", port="5000")
