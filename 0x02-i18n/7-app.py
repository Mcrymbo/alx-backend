#!/usr/bin/env python3
"""
Basic Flask app
"""
from flask import Flask, render_template, request, g
from flask_babel import Babel, _
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
    return render_template('7-index.html')

@app.before_request
def before_request():
    """ finds user and sets as global on flask.g.user """
    g.user= get_user()

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
    if request.args.get('timezone'):
        timezone = request.args.get('timezone')
        try:
            return timezone(timezone).zone
        except pytz.exceptions.UnknownTimeZoneError:
            return None
    elif g.user and g.user.get('timezone'):
        try:
            return timezone(g.user.get('timezone')).zone
        except pytz.exceptions.UnknownTimeZoneError:
            return None
    else:
        return request.accept_languages.best_match(app.config['LANGUAGES'])

babel = Babel(app, locale_selector=get_locale, timezone_selector=get_timezone)


if __name__ == '__main__':
    app.run(debug=True)
