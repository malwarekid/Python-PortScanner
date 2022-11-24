#!/bin/python3

#Building simple port scanner using python

import sys
import socket
from datetime import datetime

#define our target
if len(sys.argv) == 2:
	target = socket.gethostbyname(sys.argv[1]) #Translate hostname to IPv4
else:
	print("Invalid amount of arguments.")
	print("Syntax: python3 15_Building_Port_Scanner.py <ip>")

#adding Banner
print("-" * 120)

print("""
         ██████╗  ██████╗ ██████╗ ████████╗    ███████╗ ██████╗ █████╗ ███╗   ██╗███╗   ██╗███████╗██████╗ 
         ██╔══██╗██╔═══██╗██╔══██╗╚══██╔══╝    ██╔════╝██╔════╝██╔══██╗████╗  ██║████╗  ██║██╔════╝██╔══██╗
         ██████╔╝██║   ██║██████╔╝   ██║       ███████╗██║     ███████║██╔██╗ ██║██╔██╗ ██║█████╗  ██████╔╝
         ██╔═══╝ ██║   ██║██╔══██╗   ██║       ╚════██║██║     ██╔══██║██║╚██╗██║██║╚██╗██║██╔══╝  ██╔══██╗
         ██║     ╚██████╔╝██║  ██║   ██║       ███████║╚██████╗██║  ██║██║ ╚████║██║ ╚████║███████╗██║  ██║
         ╚═╝      ╚═════╝ ╚═╝  ╚═╝   ╚═╝       ╚══════╝ ╚═════╝╚═╝  ╚═╝╚═╝  ╚═══╝╚═╝  ╚═══╝╚══════╝╚═╝  ╚═╝

                                    						code by - Nitin Sharma""")

print("Scanning Target: " +target)
print("Time started: " +str(datetime.now()))
print("-" * 120)

try:
		for port in range(1,65535): #define range to scan ports
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #IPv4 and Port
			socket.setdefaulttimeout(.1) #waiting for 1 sec to connect
			#print("Checking ports {}".format(port))
			result = s.connect_ex((target,port)) #returns as indicator if error
			if result == 0: #for succesful connect to the port 
					print("Port {} is open".format(port))
			s.close()

except KeyboardInterrupt: #keyboard exit
		print("\nExiting program.")
		sys.exit()

except socket.gaierror: #hostname error
		print("Hostname could not be resolve.")
		sys.exit()

except socket.error: #server error 
		print("Couldn't connect to the server.")
		sys.exit()
