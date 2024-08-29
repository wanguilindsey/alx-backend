#!/usr/bin/env python3
"""
Basic Flask app with Babel for localization and user session handling
"""
from typing import Dict, Union
from flask import Flask, g, request, render_template
from flask_babel import Babel


class Config(object):
    """
    Configures supported languages and default settings
    """
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


# Initialize Flask app and load configuration
app = Flask(__name__)
app.config.from_object(Config)

# Initialize Babel for localization
babel = Babel(app)


@babel.localeselector
def get_locale() -> str:
    """
    Determines the best matching locale from the request
    """
    locale = request.args.get('locale', '').strip()
    if locale in Config.LANGUAGES:
        return locale
    return request.accept_languages.best_match(app.config['LANGUAGES'])


users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


def get_user(user_id: int) -> Union[Dict[str, Union[str, None]], None]:
    """
    Retrieves a user by ID
    """
    return users.get(user_id)


@app.before_request
def before_request():
    """
    Adds the logged-in user to the global session object `g`
    """
    g.user = get_user(int(request.args.get('login_as', 0)))


@app.route('/', strict_slashes=False)
def index() -> str:
    """
    Renders the '5-index.html' template
    """
    return render_template('5-index.html')


if __name__ == '__main__':
    app.run()
