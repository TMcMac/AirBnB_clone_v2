#!/usr/bin/python3
"""Script to use flask to get cities by statefrom sql db"""

if __name__ == '__main__':
    from flask import Flask, render_template
    from models import storage
    from models.state import State
    from operator import attrgetter

    app = Flask(__name__)

    @app.route('/states_list', strict_slashes=False)
    def state_list():
        """
        call a page that presents all state objects in storage.all
        and presents them in an unordered list in alpha order
        """
        states = storage.all('State')
        results = states.values()
        alpha_states = sorted(results, key=attrgetter('name'))
        return render_template('7-states_list.html', states=alpha_states)

    @app.route('/cities_by_states', strict_slashes=False)
    def city_state():
        """
        call a page that shows all states from storage
        and all cities by state under each state
        """
        states = storage.all('State')
        results = states.values()
        alpha_states = sorted(results, key=attrgetter('name'))
        return render_template('8-cities_by_states.html',
                               states=alpha_states)

    @app.teardown_appcontext
    def teardown(self):
        """Call close"""
        storage.close()

    app.run(host='0.0.0.0', port='5000')
