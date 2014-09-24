import shutil
import os 
import fnmatch

start_dir = "fortune1"
for dirpath, dirs, files in os.walk(start_dir):
	for single_dir in dirs:
		if fnmatch.fnmatch(single_dir, "fortune19"):
			print("Deleting ", single_dir)
			shutil.rmtree(os.path.join(dirpath, single_dir))

