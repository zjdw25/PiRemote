#!/usr/bin/env python
import cgi;
import cgitb
cgitb.enable()

NULL_CHAR = chr(0)

def write_report(report):
    fd = open('/dev/hidg0', 'rb+')
    fd.write(report.encode())
    fd.close()

def send_key(key):
  KEY = {
    'down': 81,
    'up': 96,
    'left': 80, # Press left short press for skip back 10 seconds, long press for rewind
    'right': 79, # Press right short press for skip ahead 10 seconds, long press for fast forward
    'esc': 41,
    'backspace': 42,
    'space': 44, #spacebar = media play/pause
    'enter': 40
  }
 

  if(key == ''):
    return

  write_report(NULL_CHAR*2+chr(KEY[key])+NULL_CHAR*5)
  # Press SHIFT + a = A
  #write_report(chr(32)+NULL_CHAR+chr(4)+NULL_CHAR*5)
  write_report(NULL_CHAR*8)


#print "Content-Type: text/html"
#print
form = cgi.FieldStorage()
if "action" not in form:
    print "<H1>Error</H1>"
    print "Please fill in the name and addr fields."
action = form.getvalue('action')
#print "<html><body><h2>Hello World!</h2>", action, "</body></html>"
send_key(action)
