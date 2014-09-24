import os
import fnmatch

start_dir = "fortune1"

for dirpath, dirs, files in os.walk(start_dir):
	for single_file in files:
		if fnmatch.fnmatch(single_file, "*txt"):
			print("Reading... ", single_file)
			#if second argument is not passed, then 'r' is assumed
			f = open(os.path.join(dirpath, single_file)) 
			print("File Content...")
			print(f.read())
			f.close()

