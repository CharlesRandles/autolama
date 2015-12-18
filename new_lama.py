#!/usr/bin/python

"""
CGI script to create a new LAMA.
Returns a page listing all LAMAs for this team.
"""

import database
import practices

import cgi
import cgitb
cgitb.enable()

def insert_statement(team_name, department_name, practice_list, fields):
    sql = "insert into lama (team_name, department_name, "
    values = "('{}','{}',".format(team_name, department_name)
    for practice in practice_list:
        sql += practice + ","
        values += "'{}', ".format(fields[practice].value)
    sql = sql[0:-1] + ")"
    values = values[0:-1] + ");"
    sql = sql + " values " + values
    return sql

print "Content-type: text/html"
print

html="""
<html>
  <head>
    <title>Your shiny new LAMA!</title>
  </head>
  <body>
"""
form = cgi.FieldStorage()
team_name = form['team_name'].value
team_dept = form['department_name'].value
html += "      <h3>Team: {} Dept: {}</h3>\n".format(team_name, team_dept)
practices = map(str, practices.getPractices())

for practice in practices:
    html += "      {}: {}<br />".format(practice, form[practice].value)

html += "<hr/>{}".format(insert_statement(team_name, team_dept, practices, form))

html += """
  </body>
</html>
"""

print html

