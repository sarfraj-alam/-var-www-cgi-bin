#!/usr/bin/python3

print("content-type: text/html")
print()

import subprocess as sp
import cgi

form = cgi.FieldStorage()

os_name = form.getvalue("X")

cmd = f"sudo docker stop {os_name}"

output = sp.getstatusoutput(cmd)

status = output[0]
op = output[1]

if (status == 0):
    print (f"{os_name} operating_system  stopped successfully!")
else:
    print(f"Failed to stop {os_name} operating_system with error {op}")
