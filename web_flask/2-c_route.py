#!/usr/bin/python3
"""
A basic setup file for Flask where
flask will run on 0.0.0.0 port 5000
and return hello hbnb or hbnb or text
from a specified URL
"""


if __name__ == '__main__':
    from flask import Flask
    app = Flask(__name__)

    @app.route('/', strict_slashes=False)
    def hello_world():
        """Displays hello hbhb!"""
        return 'Hello HBNB!'

    @app.route('/HBNB', strict_slashes=False)
    def show_hbnb():
        """Displays HBNB"""
        return 'HBNB'

    @app.route('/c/<text>', strict_slashes=False)
    def c_is_fun(text):
        """
        if a /c/<text> url is used, the text will
        be pulled out and returned
        """
        phrase = text.replace('_', ' ')
        return "C " + phrase

    app.run(host='0.0.0.0', port='5000')
