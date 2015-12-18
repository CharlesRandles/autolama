#!/usr/bin/python

"""
The practices we measure.
"""

import database

def getPractices():
    sql = "select name from practices;"
    cursor = database.getCursor()
    practices = []

    cursor.execute(sql)
    for row in cursor:
        practices.append(row[0])
    return practices

