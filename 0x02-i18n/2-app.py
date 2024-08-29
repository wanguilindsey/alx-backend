#!/usr/bin/env python3
"""
Basic Flask application with Babel for language localization
"""
from flask import Flask, request, render_template
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
    Selects best matching locale from request
    """
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/', strict_slashes=False)
def index() -> str:
    """
    Renders the '2-index.html' template
    """
    return render_template('2-index.html')


if __name__ == '__main__':
    app.run()
