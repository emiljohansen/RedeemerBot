import sqlite3

conn = None


def init():
    conn = sqlite3.connect(':memory:')
    c = conn.cursor()
    #Create Tables
    c.execute("CREATE TABLE banned_users (uid, uname, banned_date reason)")

    #What other tables are required?

    conn.commit()

def save(tablename: str, values: tuple):
    return

def update(tablename: str, values: tuple):
    return

def delete(tablename: str, values: tuple):
    return

def get(tablename: str, values: tuple):
    return