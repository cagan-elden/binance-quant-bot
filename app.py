# library imports
import binance
import requests
import flask
import sqlite3
import json

import main

# start app
app = flask.Flask(__name__)

@app.route('/')
def index():
    return flask.render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)