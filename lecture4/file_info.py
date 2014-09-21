import os

#os.path.join uses the system-spcific path join to build path
homework_dir_path=os.path.join(os.getcwd(), "homework")

homework_file_path=os.path.join(os.getcwd(), "homework", "data_load.py")

symbolic_link="/python_git"

bogus_path=os.path.join(os.getcwd(), "homework", "bogus.py")


print("isfile1:", os.path.isfile(homework_dir_path))
print("isfile2:", os.path.isfile(homework_file_path))
#Output
#isfile1: False
#isfile2: True

print("isdir1:", os.path.isdir(homework_dir_path))
print("isdir2:", os.path.isdir(homework_file_path))
#Output
#isdir1: True
#isdir2: False

print("islink1:", os.path.islink(homework_dir_path))
print("islink2:", os.path.islink(symbolic_link))
#Output
#islink1: False
#islink2: True

print("getsize1", os.path.getsize(homework_dir_path))
print("getsize2", os.path.getsize(homework_file_path))
#Output
#getsize1 204
#getsize2 13663


#os.path.getmtime - returns last modified date/time
#time is returned as number of seconds since the epoch
print("getmtime1", os.path.getmtime(homework_dir_path))
print("getmtime2", os.path.getmtime(homework_file_path))
#Output
#getmtime1 1411307744.0
#getmtime2 1411307630.0


#os.path.getatime - returns last accessed date/time
#time is returned as number of seconds since the epoch
print("getatime1", os.path.getatime(homework_dir_path))
print("getatime2", os.path.getatime(homework_file_path))
#Output
#getatime1 1411307744.0
#getatime2 1411307737.0