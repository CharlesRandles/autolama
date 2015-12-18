#!/usr/bin/python

"""
CGI script to create a new LAMA.
Returns a page listing all LAMAs for this team.
"""

import database

import cgi
import cgitb
cgitb.enable()

print "Content-type: text/text"
print

print "Your lama:"
