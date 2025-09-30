import sqlite3
from database import tables

# appsettling
def connectDatabase():
    conn = sqlite3.connect('database.db')
    return conn

def createDatabase():
    conn = connectDatabase()
    cur = conn.cursor()
    for table in tables.klines:
        cur.execute(table)
    conn.close()

# interactive stuff
def createCursor(conn):
    cur = conn.cursor()
    return cur

def sqlQueryProcessor(conn, cur, query, queryType, fetchMode):
    if queryType == 'insert' or queryType == 'update':
        cur.execute(query)
        conn.commit()
        val = 1
    elif queryType == 'select':
        cur.execute(query)

        if fetchMode == 1: val = cur.fetchall(); return val
        val = cur.fetchone()

    conn.close()
    return val