#!/usr/bin/python3
"""This script starts a Flask web application"""
from flask import Flask
from flask import render_template

app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/states_list/')
def states_list():
    return render_template('7-states_list.html')