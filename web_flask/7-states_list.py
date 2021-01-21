#!/usr/bin/python3
"""Script to use flask to get cities by statefrom sql db"""

if __name__ == '__main__':
    from flask import Flask, render_template
    from models import storage
    from models.state import State

    app = Flask(__name__)
    
    @app.teardown_appcontext
    def teardown(self):
        """Call close"""
        storage.close()

    @app.route('/states_list', strict_slashes=False)
    def state_list():
        """
        call a page that presents all state objects in storage.all
        and presents them in an unordered list in alpha order
        """
        states = storage.all('State').values()
        for state in states:
            print(state)
        return render_template('7-states_list.html', states=states)


    app.run(host='0.0.0.0', port='5000')
