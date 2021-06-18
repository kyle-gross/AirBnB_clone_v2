#!/usr/bin/python3
"""This script starts a Flask web application"""
from flask import Flask
from flask import render_template
from models import storage

app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/states_list/')
def states_list():
    # state_list = []
    # state_dict = storage.all(State)
    # for k, v in state_dict.items():
    #     string = ""
    #     if v == 'name', 'id':
    #         string = state_dict[k] + ': ' + state_dict[v]
    state_dict = storage.all(State)
    new_dict = {}
    for val in state_dict.values():
        for k, v in val.items():
            if k == 'name':
                new_dict[k] = v
            if k == 'id':
                new_dict[k] = v
    new_list = sorted(new_dict.items(), key=lambda x:x[1])
    sort_dict = dict(new_list)

    return render_template('7-states_list.html',
                           State=sort_dict)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
