#!/usr/bin/env python3
"""
Basic Flask application with Babel for localization
"""
from flask import Flask, render_template
from flask_babel import Babel


class Config(object):
    """
    Configuration for supported languages and default settings
    """
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


# Instantiate Flask app and load configuration
app = Flask(__name__)
app.config.from_object(Config)

# Initialize Babel for app localization
babel = Babel(app)


@app.route('/', strict_slashes=False)
def index() -> str:
    """
    Renders the '1-index.html' template
    """
    return render_template('1-index.html')


if __name__ == '__main__':
    app.run()
