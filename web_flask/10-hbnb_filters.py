#!/usr/bin/python3
"""This script starts a Flask web application"""
from models.amenity import Amenity
from models.city import City
from flask import Flask, render_template
from models import storage
from models.state import State

app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/hbnb_filters/')
def city_list():
    state_dict = storage.all(State)
    sorted_dict = sorted(state_dict.values(), key=lambda x: x.name)
    city_dict = storage.all(City)
    sorted_city = sorted(city_dict.values(), key=lambda x: x.name)
    amenity_dict = storage.all(Amenity)
    sorted_amenity = sorted(amenity_dict.values(), key=lambda x: x.name)
    return render_template('10-hbnb_filters.html', state=sorted_dict,
                           city=sorted_city, amenity=sorted_amenity)


@app.teardown_appcontext
def teardown(error):
    if storage:
        storage.close()


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
