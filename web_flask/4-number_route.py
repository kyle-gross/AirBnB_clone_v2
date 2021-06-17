#!/usr/bin/python3
"""This module contains a script which starts Flask"""
from flask import Flask

hbnb = Flask(__name__)
hbnb.url_map.strict_slashes = False


@hbnb.route('/')
def func():
    """Displays 'Hello HBNB!'"""
    return 'Hello HBNB!'


@hbnb.route('/hbnb')
def func1():
    """Displays 'HBNB'"""
    return 'HBNB'


@hbnb.route('/c/<text>')
def func2(text):
    """Displays 'C <text>'"""
    return 'C %s' % text.replace('_', ' ')


@hbnb.route('/python/<string:text>')
@hbnb.route('/python/')
def func3(text='is cool'):
    """Displays 'Python <text>'"""
    return 'Python %s' % text.replace('_', ' ')


@hbnb.route('number/<int:n>')
def func4(n):
    """Determines if <n> is a number!!!!"""
    return '%i is a number' % n


if __name__ == '__main__':
    hbnb.run(debug=True, host='0.0.0.0')
