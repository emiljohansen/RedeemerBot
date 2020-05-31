import sqlite3

conn = None


def init():
    conn = sqlite3.connect(':memory:')
    c = conn.cursor()
    #Create Tables
    c.execute("CREATE TABLE banned_users (uid, uname, banned_date, reason)")
    c.execute("CREATE TABLE moderators (uid, uname, admin)")
    c.execute("CREATE TABLE planned_runs (id, run_name, host, participants)")
    c.execute("CREATE TABLE approved_hosts (uid, uname)")

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

def get_all(tablename: str):
    return conn.cursor().execute("SELECT * FROM %s".format(tablename))