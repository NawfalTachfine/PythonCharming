#!/usr/bin/python2
# -*- coding: utf-8 -*-
__author__ = 'NawfalTachfine'

# Important Note
# The standard network byte order is big endian, so convert when working
# with little endian systems

# ------------------------------------------------------------------------------

# Capturing Packets - run the bad boy with python2 !!!!
import pcapy  # Py implementation of the packet capture library

# let's see what devices we have here
devs = pcapy.findalldevs()
print(devs)

# opening a device, using it's number, number of bytes to get per packet
# (max 65536), promiscuous mode(get irrelevent data) , and timout(ms)
# we get a handle on the received stream
cap = pcapy.open_live("eth0", 65536, 1, 0)

count = 1
while count < 100:
	(header, payload) = cap.next()
	print(count)
	count = count + 1

quit()

# ------------------------------------------------------------------------------

# Simple HTTP Request
import http.client

h = http.client.HTTPConnection("www.infiniteskills.com")
h.request("GET", "/")
data = h.getresponse()
print("Here's the code bro")
print(data.code)
print("Here are the headers")
print(data.headers)
print("And now the actual data")
text = data.readlines()
for t in text:
	print(t.decode('utf-8'))

quit()

# ------------------------------------------------------------------------------

# Grabbing Banners = server info
import socket
import re

sock = socket.socket( socket.AF_INET, socket.SOCK_STREAM )
# internet family / stream => TCP

sock.connect( ("www.microsoft.com", 80) )

http_get = b"GET / HTTP/1.1\nHost: www.microsoft.com\n\n"
data = ''

try:
	sock.sendall(http_get) # sending http get
	data = sock.recvfrom(1024) # receiving first 1024 bytes of data
except socket.error:
	print("Socket error dude!", socket.errno)
finally:
	print("Closing da connexion")
	sock.close()


strdata = data[0].decode("utf-8")
headers = strdata.splitlines()

for s in headers:
	if re.search('Server:', s): # looking for the server field
		s = s.replace("Server: ", "")
		print(s)

quit()

# ------------------------------------------------------------------------------

# Network Server
import socket

size = 512
host = ''
port = 9898

sock = socket.socket( socket.AF_INET, socket.SOCK_STREAM )
# internet family / stream => TCP

sock.setsockopt( socket.SOL_SOCKET, socket.SO_REUSEADDR, 1 )

sock.bind( (host, port) ) # binding to particular host and port
sock.listen(5) # listening to up to 5 people

c, addr = sock.accept() # client connexion and address of remote end

data = c.recv( size ) # recieving data from client socket, up to 512 bytes
if data:
	f = open("storage.dat", '+w')
	print("connexion from: ", addr[0])
	f.write(addr[0])
	f.write(":")
	f.write(data.decode("utf-8")) # convert data from bytes into string
	f.close()
sock.close()

# use "nc localhost 9898" to send messages and try this thing

quit()

# ------------------------------------------------------------------------------

# Network Client
import socket

host = 'localhost'
mysock = socket.socket( socket.AF_INET, socket.SOCK_STREAM )
# internet family / stream => TCP

addr = (host, 5555)
mysock.connect(addr)

try:
	msg = b"howdie, this is a test\n"
	mysock.sendall(msg)
except socket.errno as e:
	print("Socket error dude! ", e)
finally:
	mysock.close()

# To test this you need to be listening on port 5555 using netcat for ex
# nc -l 5555
quit()

# ------------------------------------------------------------------------------

# Name Server Lookups
import socket

print( socket.gethostbyaddr("8.8.8.8") )
print( socket.gethostbyname("www.google.com") )

quit()

# ------------------------------------------------------------------------------
