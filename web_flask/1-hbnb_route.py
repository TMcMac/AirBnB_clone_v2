#!/usr/bin/python3
"""
A basic setup file for Flask where
flask will run on 0.0.0.0 port 5000
and return hello hbnb or hbnb
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

    app.run(host='0.0.0.0', port='5000')
