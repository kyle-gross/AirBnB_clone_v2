#!/usr/bin/python3
"""This script starts a Flask web application"""
from flask import Flask
from flask import render_template
from models import storage

app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/states_list/')
def states_list():
    return render_template('7-states_list.html',
                           State=storage.all(State)[name].sort())


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
