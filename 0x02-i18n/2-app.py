#!/usr/bin/env python3
""" get_locale function """
from flask import Flask, render_template
from flask_babel import Babel

app = Flask(__name__)
babel = Babel(app)


class Config(object):
    """ class for defining defaults """
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app.config.from_object('1-app.Config')


@app.route('/', methods=['GET'], strict_slashes=False)
def index() -> str:
    """ route for 1-index.html
    """
    return render_template('1-index.html')


@babel.localeselector
def get_locale() -> str:
    """ determine best language """
    return request.accept_languages.best_match(app.config['LANGUAGES'])


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
