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

print "Your lama:"

form = cgi.FieldStorage()
practices = map(str, practices.getPractices())
for practice in practices:
    print practice + "=" + form[practice]
