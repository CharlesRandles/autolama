#!/usr/bin/python

import cgi
import cgitb
import database
import practices
import lama
cgitb.enable()

print "Content-type: text/html"
print

html="""
<html>
  <head>
    <title>A Lama.</title>
  </head>
  <body>
"""    
form = cgi.FieldStorage()
lamaId = form['id'].value
found_lama = lama.Lama.findById(lamaId)
html += found_lama.to_html()
html += """
  </body>
</html>  
"""

print html

html += """
  </body>
  </html>
"""
