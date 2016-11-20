#!/usr/bin/python3
__author__ = 'NawfalTachfine'

# ------------------------------------------------------------------------------

# Classes & Instances

class me:
	def __init__(self, foo):
		self.myvar = foo

	def getval(self):
		return self.myvar

	def setval(self, y):
		self.myvar = y

my1 = me("ziisss")
my2 = me("iiizzz")
my3 = me("spartaaaa")
x = my1.getval()
print(x)
x = my2.getval()
print(x)
my3.setval("testing.. SPARTAAA!")
x = my3.getval()
print(x)

quit()

# ------------------------------------------------------------------------------

# Handling Exceptions
try:
	fhandle = open("dummy", "w")
	fhandle.write("This is the content of the file")
	print("Woohoo! Wrote some stuff into the file")
except IOError:
	print("I caught me an exception here: unable to write to the darn file")
except:
	print("I have no idea what happened")
else:
	print("GREAT SUCCESS! I LIKE!")
	fhandle.close()

# ------------------------------------------------------------------------------

# Parsing Arguments
import argparse

parser = argparse.ArgumentParser( description="This program can achieve world peace" )
parser.add_argument( '-i', type=str, help="This is a necessary parameter", required=True)
parser.add_argument( '-o', type=str, help="This is an optional parameter", required=False)

# cmdargs ends up being a dictionary/hash
cmdargs = parser.parse_args()

# access the parameter based on the flag
ivar = cmdargs.i
print( ivar )
print( cmdargs.o )

# ------------------------------------------------------------------------------

# System Calls
import os
from subprocess import call

# the os interface can give access to system information
print( os.getcwd() ) # current working directory
print( os.getuid() ) # user ID
print( os.getenv("PATH") ) # environment variable, PATH in this case

# system enables the calling of outside programs, call is similar
os.system("ls ../ -la")
inp = input("Hit Enter")
call(["ls", "-la"])

# ------------------------------------------------------------------------------

# Threads
import threading

class aThread(threading.Thread):
	def __init__(self, num, val):
		threading.Thread.__init__(self)
		self.threadNum = num
		self.loopCount = val

	def run(self):
		print("Starting run: ", self.threadNum)
		myfunc(self.threadNum, self.loopCount)

def myfunc(num, val):
	count = 0
	while count < val:
		print( num, " : ", val*count )
		count +=1

t1 = aThread(1, 15)
t2 = aThread(2, 20)
t3 = aThread(3, 25)
t4 = aThread(4, 30)

t1.start()
t2.start()
t3.start()
t4.start()

threads = []
threads.append(t1)
threads.append(t2)
threads.append(t3)
threads.append(t4)

for t in threads:
	t.join()

# ----------------------------------------------------------------------------------------------------------------------
