#!/usr/bin/python3
"""This script starts a Flask web application"""
from models.city import City
from flask import abort, Flask, render_template
from models import storage
from models.state import State

app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/states/')
@app.route('/states/<uuid:id>')
def city_list(id=0):
    new_dict = {}
    # Create sorted State dict
    state_dict = storage.all(State)
    for state in state_dict.values():
        if str(id) == state.id:
            # Reduce to one state
            new_dict['name'] = state.name
            new_dict['id'] = state.id
            break
    if new_dict:
        # Create sorted City dict
        city_dict = storage.all(City)
        sorted_city = sorted(city_dict.values(), key=lambda x: x.name)
        # Render template with 1 sorted dict and 1 state only dict
        return render_template('9-states.html', state=new_dict,
                               city=sorted_city, id=0)
    if id == 0:
        sorted_dict = sorted(state_dict.values(), key=lambda x: x.name)
        return render_template('9-states.html', state=sorted_dict,
                               city=None, id=1)

    else:
        return render_template('9-states.html', state=None,
                               city=None, id=2)


@app.teardown_appcontext
def teardown(error):
    if storage:
        storage.close()


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
