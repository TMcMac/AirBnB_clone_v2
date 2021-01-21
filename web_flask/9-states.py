#!/usr/bin/python3
"""Script to use flask to get cities by statefrom sql db"""

if __name__ == '__main__':
    from flask import Flask, render_template
    from models import storage
    from models.state import State
    from operator import attrgetter

    app = Flask(__name__)

    @app.route('/states', strict_slashes=False)
    @app.route('/states/<sid>', strict_slashes=False)
    def state_list(sid=None):
        """
        call a page that presents all state objects in storage.all
        and presents them in an unordered list in alpha order
        If a state object id number is supplied get only that state
        and send it to the html file to print state and cities
        """
        states = storage.all('State')
        results = states.values()
        if sid is None:
            alpha_states = sorted(results, key=attrgetter('name'))
            return render_template('9-states.html',
                                   states=alpha_states, sid=sid)
        else:
            for state in results:
                if state.id == sid:
                    return render_template('9-states.html',
                                           states=state, sid=state.id)
            return render_template('9-states.html', states=None, sid=sid)

    @app.teardown_appcontext
    def teardown(self):
        """Call close"""
        storage.close()

    app.run(host='0.0.0.0', port='5000')
