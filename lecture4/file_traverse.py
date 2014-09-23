import os
import fnmatch

start_dir = "fortune1"
for dirpath, dirs, files in os.walk(start_dir):
	for single_file in files:
		if fnmatch.fnmatch(single_file, "*log"):
			print("Deleting ", single_file)
			print(os.path.join(dirpath, single_file))
			os.remove(os.path.join(dirpath, single_file))

