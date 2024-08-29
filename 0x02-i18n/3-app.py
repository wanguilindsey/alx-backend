#!/usr/bin/env python3
"""
Basic Flask app with Babel for localization
"""
from flask import Flask, request, render_template
from flask_babel import Babel


class Config(object):
    """
    Configures supported languages and defaults
    """
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


# Initialize Flask app and load config
app = Flask(__name__)
app.config.from_object(Config)

# Initialize Babel for app localization
babel = Babel(app)


@babel.localeselector
def get_locale() -> str:
    """
    Selects the best matching locale from the request
    """
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/', strict_slashes=False)
def index() -> str:
    """
    Renders the '3-index.html' template
    """
    return render_template('3-index.html')


if __name__ == '__main__':
    app.run()
