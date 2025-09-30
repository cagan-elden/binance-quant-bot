# library imports
import binance
import requests
import flask
import sqlite3
import json

import main
import api

from api import get_klines, account

client = get_klines.api_connection()
account_value = account.account_value(client)

# start app
app = flask.Flask(__name__)

@app.route('/')
def index():
    return flask.render_template('index.html', balance=account_value)

if __name__ == '__main__':
    app.run(debug=True)