#!/usr/bin/python3
"""This script starts a Flask web application"""
from models.city import City
from flask import Flask, render_template
from models import storage
from models.state import State

app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/cities_by_states/')
def city_list():
    # Create sorted State dict
    state_dict = storage.all(State)
    sorted_dict = sorted(state_dict.values(), key=lambda x: x.name)
    # Create sorted City dict
    city_dict = storage.all(City)
    sorted_city = sorted(city_dict.values(), key=lambda x: x.name)
    # Render template with 2 sorted dicts
    return render_template('8-cities_by_states.html', state=sorted_dict,
                           city=sorted_city)


@app.teardown_appcontext
def teardown(error):
    if storage:
        storage.close()


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
