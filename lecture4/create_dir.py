import os

print("Current Direcotry:",os.getcwd())

print("Trying to create new directory structure...")

for i in range(0,10):
	directory = "test" + str(i)
	if(not os.path.exists(directory)):
		os.mkdir(directory) #create a directory
		os.chdir(directory) #change directory
		print("Created ", directory)
	else:
		print("Cannot create a directory {0}, already exists", directory)
