import cgi
import cgitb
import database
import practices
cgitb.enable()

print "Content_type: text/html"
print

html="""
<html>
  <head>
    <title>A Lama.</title>
  </head>
  <body>
"""    
form = cgi.FieldStorage()
lamaId = form[id].value()
sql = "select * from lama where id=?"
cursor = database.getCursor().execute(sql, id)
html += cursor.fetchone()
html += """
  </body>
</html>  
"""

print html

html += """
  </body>
  </html>
"""