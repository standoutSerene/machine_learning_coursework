## Python Sys Module

# - provides access to variables and functions related to system or python interpreter
# - argv -- stores the list of command line arguments


import sys

#def printData():
#	print(sys.argv)
#	print(type(sys.argv))

#printData()

# argv[0] contains the file name, which is given while compiling as a command line argument 

#def printSum():
#	print(int(sys.argv[1])+int(sys.argv[2]))

#printSum() 

print(sys.version)
print(sys.path)  # interpreter will search for packages in these paths
print(sys.maxsize)	
print(type(	sys.stdin))
print(sys.stdout)