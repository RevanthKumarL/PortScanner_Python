#!/bin/python

# python3 scanner.py <ip>

import sys  
import socket #for node to node connection
from datetime import datetime

#define the target

if len(sys.argv) == 2:
	target = socket.gethostbyname(sys.argv[1])#translating hostname to IPv4
	#dns to IPv4 if the given target is something like kalirev
else:
	print("Invalid amount of arguments.")
	print("Syntax: python3 scanner.py <ip>")
	
#and a banner just like that

print("*" * 50)
print("Scanning Target "+target)
print("Time Started: "+str(datetime.now()))
print("*" * 50)

try: 
	for port in range(1,1024):
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		socket.setdefaulttimeout(0.0000001)
		result = s.connect_ex((target,port))#returns error indicator
		if result == 0:
			print("Port {} is open".format(port))
		s.close()
		
except KeyboardInterrupt:
	print("\nExisting program.")
	sys.exit()
	
except socket.gaierror:
	print("Hostname could not be resolved.")
	sys.exit()
	
except socket.error:
	print("Couldn't connect to server.")
	sys.exit()


