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

print "Content-type: text/html"
print

html="""
<html>
  <head>
    <title>Your shiny new LAMA!</title>
  </head>
  <body>
"""
print "Your lama:"

form = cgi.FieldStorage()
team_name = form['team_name'].value
team_dept = form['department_name'].value
html += "      <h3>Team: {} Dept: {}</h3>\n".format((team_name, team_dept))
practices = map(str, practices.getPractices())
for practice in practices:
    html += "      {}: {}<br />".format((practice, form[practice].value))

html += """
  </body>
</html>
"""

print html

