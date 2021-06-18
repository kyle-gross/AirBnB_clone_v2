#!/usr/bin/python3
"""This script starts a Flask web application"""
from flask import Flask, render_template
from models import storage

app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/states_list')
def states_list():
    state_dict = storage.all(State)
    sorted_dict = sorted(state_dict.values(), key=lambda x: x.name)
    return render_template('7-states_list.html', State=sorted_dict)


@app.teardown_appcontext
def teardown(error):
    if storage:
        storage.close()


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
