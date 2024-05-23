import sqlite3

def dict_factory(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d

def get_from_db(query, many=False):
    con = sqlite3.connect('database.db')
    con.row_factory = dict_factory
    cur = con.cursor()
    cur.execute(query)
    if many:
        res = cur.fetchall()
    else:
        res = cur.fetchone()
    con.close()
    return res

def insert_to_db(query):
    con = sqlite3.connect('database.db')
    cur = con.cursor()
    cur.execute(query)
    con.commit()
    con.close()
