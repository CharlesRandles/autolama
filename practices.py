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

""" Practices are:
insert into practices (name) values ('standups');
insert into practices (name) values ('retrospectives');
insert into practices (name) values ('backlog_management');
insert into practices (name) values ('product_ownership');
insert into practices (name) values ('iteration_management');
insert into practices (name) values ('track_and_visualise_progress');
insert into practices (name) values ('building_quality_in');
insert into practices (name) values ('adaptive_planning');
"""
