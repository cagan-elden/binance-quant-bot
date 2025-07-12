import sqlite3
from database import tables

def connectDatabase():
    conn = sqlite3.connect('database.db')
    return conn

def createDatabase():
    conn = connectDatabase()
    cur = conn.cursor()
    for table in tables.klines:
        cur.execute(table)
    conn.close()