#!/usr/bin/python3
"""
A basic setup file for Flask where
flask will run on 0.0.0.0 port 5000
and return hello hbnb or hbnb or text
from a specified URL
"""


if __name__ == '__main__':
    from flask import Flask, render_template
    app = Flask(__name__)

    @app.route('/', strict_slashes=False)
    def hello_world():
        """Displays hello hbhb!"""
        return 'Hello HBNB!'

    @app.route('/hbnb', strict_slashes=False)
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

    @app.route('/python', defaults={'text': None}, strict_slashes=False)
    @app.route('/python/<text>', strict_slashes=False)
    def python_is_cool(text):
        """
        takes the text from the url and returns
        is in a phrase or a default
        """
        if text is None:
            phrase = "is cool"
        else:
            phrase = text.replace('_', ' ')

        return "Python " + phrase

    @app.route('/number/<int:n>', strict_slashes=False)
    def number_n(n):
        """
        if n is an int, return a phrase
        """
        return str(n) + " is a number"

    @app.route('/number_template/<int:n>', strict_slashes=False)
    def template_n(n):
        """
        If n is a valid int an html
        template with n will be rendered
        """
        return render_template('5-number.html', number=n)

    @app.route('/number_odd_or_even/<int:n>/', strict_slashes=False)
    def odd_even(n):
        """
        If n is an integer, renders a page
        based on if n is odd or even
        """
        return render_template('6-number_odd_or_even.html', number=n)

    app.run(host='0.0.0.0', port='5000')
