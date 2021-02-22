#!/usr/bin/python3

print ("content-type: text/html")
print ()

import subprocess as sp
import cgi

form = cgi.FieldStorage()

os_name = form.getvalue("X")

img_name = form.getvalue("image_name")

cmd = f"sudo docker run -dit --name {os_name} {img_name}"

output = sp.getstatusoutput(cmd)

status = output[0]
op = output[1]

if (status == 0):
    print (f"{os_name} operating system launched successfully!")
else:
    print (f"Failed to launch {os_name} operating system with error {op}!")
