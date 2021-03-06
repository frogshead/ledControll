# -*- coding: utf-8 -*-
"""
    jQuery Example
    ~~~~~~~~~~~~~~

    A simple application that shows how Flask and jQuery get along.

    :copyright: (c) 2015 by Armin Ronacher.
    :license: BSD, see LICENSE for more details.
"""
from flask import Flask, jsonify, render_template, request
app = Flask(__name__)


@app.route('/_add_numbers')
def add_numbers():
    """Add two numbers server side, ridiculous but well..."""
    c = request.args.get('c', 0, type=int)
    print c
    return jsonify(result = c)


@app.route('/')
def index():
    return render_template('index.html')
    
    
if __name__ == '__main__':
	app.debug=True
	app.run(host='0.0.0.0')
