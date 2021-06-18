#!/usr/bin/python3
"""This script starts a Flask web application"""
from flask import Flask
from flask import render_template
from models import storage

app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/states_list/')
def states_list():
    state_dict = storage.all(State)
    sorted_dict = sorted(new_dict.values(), key=lambda x: x.name)

    return render_template('7-states_list.html', State=sorted_dict)

@app.teardown_appcontext
def tear_down():
    storage.close()

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
