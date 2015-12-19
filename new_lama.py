#!/usr/bin/python

"""
CGI script to create a new LAMA.
Returns a page listing all LAMAs for this team.
"""

import database
import lama
import cgi
import cgitb

cgitb.enable()

def insertStatement(team_name, department_name, practice_list, fields):
    sql = "insert into lama (team_name, department_name, "
    values = "('{}','{}',".format(team_name, department_name)
    for practice in practice_list:
        sql += practice + ","
        values += "'{}',".format(fields[practice].value)
    sql = sql[0:-1] + ")"
    values = values[0:-1] + ");"
    sql = sql + " values " + values
    return sql

def getLamaIds(team_name):
    cursor = database.getCursor()
    sql= "select id from lama where team_name=?"
    lamas = cursor.execute(sql, (team_name,))
    lamaIds = []
    for id in lamas:
        lamaIds.append(id[0])
    return lamaIds

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
results={}
results['standups']=form['standups'].value
results['retrospectives']=form['retrospectives'].value
results['backlog_management']=form['backlog_management'].value
results['product_ownership']=form['product_ownership'].value
results['iteration_management']=form['iteration_management'].value
results['track_and_visualise_progress']=form['track_and_visualise_progress'].value
results['building_quality_in']=form['building_quality_in'].value
results['adaptive_planning']=form['adaptive_planning'].value
new_lama=lama.Lama(lama.Team(team_name, team_dept), results)

#Save it!
new_lama.write()
                   
html += new_lama.to_html()

#Get LAMAs for this team.
lamas=getLamaIds(team_name)
html += "      <ul>"
for lama_id in lamas:
    html += '        <li><a href="show_lama.py?id={}">{}</a></li>\n'.format(lama_id, "Lama {}".format(lama_id))

html += "      </ul>"
html += """
  </body>
</html>
"""

print html

