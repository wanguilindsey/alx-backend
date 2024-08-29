#!/usr/bin/env python3
"""
Basic Flask application
"""
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def index() -> str:
    """
    Renders the '0-index.html' template.
    """
    return render_template('0-index.html')


if __name__ == '__main__':
    app.run()
