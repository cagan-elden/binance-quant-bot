# app imports
from database.database import createDatabase
from api import get_klines

client = get_klines.api_connection()
symbols = get_klines.getSymbols(client)

print(symbols)