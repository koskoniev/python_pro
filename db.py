import sqlite3

def get_from_db(query):
    con = sqlite3.connect('database.db')
    # con.
    cur = con.cursor()