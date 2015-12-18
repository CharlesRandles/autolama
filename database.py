#!/usr/bin/python

"""Database access functions"""

import sqlite3

DB = 'autolama.db'
db = sqlite3.connect(DB)

def getCursor():
    return db.cursor()

def execute(sql, params):
    cursor = db.cursor()
    cursor.execute(sql, params)
    db.commit()
    cursor.close()

def executeDirect(sql):
    cursor = db.cursor()
    cursor.execute(sql)
    db.commit()
    cursor.close()
    
def commit():
    db.commit()

def close():
    db.close()
