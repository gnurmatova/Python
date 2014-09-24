import os
import shutil
import fnmatch

start_dir = "fortune1"
to_dir = "destination"
for dirpath, dirs, files in os.walk(start_dir):
	for single_file in files:
		if fnmatch.fnmatch(single_file, "*txt"):
			print("Copying {0} to {1} folder".format(single_file, to_dir))
			shutil.copy(os.path.join(dirpath, single_file), to_dir)

