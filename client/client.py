#!/usr/bin/python
import socket
cl_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ip = str(raw_input("Enter IP Address: "))
try:
	port = int(raw_input("Enter Port Number: "))
except:
	print "Invalid Port Number!"
	exit()
try:
	cl_socket.connect((ip,port))
	print "Conneted to server!"
except:
	print "Failed to Connect!"
	exit()
file_name = raw_input("Enter file name to send: ")
try:
	f = open(file_name,'r')
	cl_socket.send(file_name)
	print "Sending file...",
	cl_socket.sendall(f.read())
	print " Done!"
except:
	print "No such file exists!"
