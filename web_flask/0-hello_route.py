#!/usr/bin/python3
"""
A basic setup file for Flask where
flask will run on 0.0.0.0 port 5000
and return hello hbnb!
"""


if __name__ == '__main__':
    from flask import Flask
    app = Flask(__name__)


    @app.route('/', strict_slashes=False)
    def hello_world():
        """Displays hello hbhb!"""
        return 'Hello HBNB!'

    app.run(host='0.0.0.0', port='5000')
