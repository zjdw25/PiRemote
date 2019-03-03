#!/usr/bin/env python
import cgi;
import cgitb
cgitb.enable()



print "Content-Type: text/html"
print
print "<html><body>"
cgi.test()
print "</body></html>"
