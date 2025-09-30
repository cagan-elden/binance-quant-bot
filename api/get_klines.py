import sqlite3
import binance
import json

from binance import Client

def api_connection():
    with open('appsettling.json', 'r') as apiInfo:
        api = json.load(apiInfo)

    api_key    = api['api']['api_key']
    api_secret = api['api']['api_secret']

    client = Client(api_key, api_secret)

    return client

def getSymbols(client):
    exchangeInfo = client.get_exchange_info()

    symbols = []
    for symbol in exchangeInfo['symbols']:
        if symbol['status'] == 'TRADING' and symbol['quoteAsset'] == 'USDT':
            symbols.append(symbol['symbol'])

    return symbols

def getExchangeInfo(client, symbol):
    symbolInfo = client.get_ticker(symbol=symbol)

    return symbolInfo