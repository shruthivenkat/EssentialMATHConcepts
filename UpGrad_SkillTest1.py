# you have to construct a pyramid 
 # |N = 3|
#              ##*##
#              #***#
#              *****


from __future__ import print_function
import sys

n=input("enter the number of steps")

count = n-1
star = 1

for i in range(0,n+1):
	for j in range(0, count+1):
		sys.stdout.write("#")
	for k in range(0,star):
		sys.stdout.write("*")
	for p in range(0, count+1):
		sys.stdout.write("#")
	print("\n")
	count = count - 1
	star = star + 2

sys.stdout.flush() 


