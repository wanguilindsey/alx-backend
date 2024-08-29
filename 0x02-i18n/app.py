#!/usr/bin/env python3
"""
Basic Flask application with user locale and timezone handling
"""
import pytz
import datetime
from typing import Dict, Union
from flask import Flask, g, request, render_template
from flask_babel import Babel, format_datetime


class Config(object):
    """
    Configuration class for the app
    """
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


# Initialize Flask app and load configuration
app = Flask(__name__)
app.config.from_object(Config)

# Initialize Babel for localization and timezone handling
babel = Babel(app)


users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


def get_user(user_id: int) -> Union[Dict[str, Union[str, None]], None]:
    """
    Retrieves user details by ID
    """
    return users.get(user_id, None)


@babel.localeselector
def get_locale() -> str:
    """
    Selects the best matching locale from request or user settings
    """
    options = [
        request.args.get('locale', '').strip(),
        g.user.get('locale', None) if g.user else None,
        request.accept_languages.best_match(app.config['LANGUAGES']),
        Config.BABEL_DEFAULT_LOCALE
    ]
    for locale in options:
        if locale in Config.LANGUAGES:
            return locale


@babel.timezoneselector
def get_timezone() -> str:
    """
    Selects the best matching timezone from request or user settings
    """
    tz = request.args.get('timezone', '').strip()
    if not tz and g.user:
        tz = g.user.get('timezone', '')
    try:
        return pytz.timezone(tz).zone
    except pytz.exceptions.UnknownTimeZoneError:
        return app.config['BABEL_DEFAULT_TIMEZONE']


@app.before_request
def before_request() -> None:
    """
    Sets user and current time in global session object `g`
    """
    g.user = get_user(int(request.args.get('login_as', 0)))
    g.time = format_datetime(datetime.datetime.now())


@app.route('/', strict_slashes=False)
def index() -> str:
    """
    Renders the main HTML template
    """
    return render_template('index.html')


if __name__ == '__main__':
    app.run()
