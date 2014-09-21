import os

#os.path.join uses the system-spcific path join to build path
homework_dir_path=os.path.join(os.getcwd(), "homework")

homework_file_path=os.path.join(os.getcwd(), "homework", "data_load.py")

symbolic_link="/python_git"

bogus_path=os.path.join(os.getcwd(), "homework", "bogus.py")

print("My Path is:")
print(homework_dir_path)
#Output
#My Path is:
#/Users/gulanurmatova/Documents/UNH/Python/git/lecture4/homework

#os.path.exists validates the path
print("exists1:",os.path.exists(homework_file_path))
print("exists2:",os.path.exists(bogus_path))
#Output
#exists1: True
#exists2: False

#directory of the given path
print("dirname1:",os.path.dirname(homework_dir_path))
print("dirname2:",os.path.dirname(homework_file_path))
#Output
#dirname1: /Users/gulanurmatova/Documents/UNH/Python/git/lecture4
#dirname2: /Users/gulanurmatova/Documents/UNH/Python/git/lecture4/homework


#os.path.commonprefix does character comparison to identify the common path
print("commonprefix1:",os.path.commonprefix([homework_file_path, homework_dir_path, symbolic_link]))
print("commonprefix2:",os.path.commonprefix([homework_file_path, homework_dir_path, bogus_path]))
#Output
#commonprefix1: /
#commonprefix2: /Users/gulanurmatova/Documents/UNH/Python/git/lecture4/homework


#os.path.split - splits the path to passed file/directory from the file/directory
print("split1:",os.path.split(homework_dir_path))
print("split2:",os.path.split(homework_file_path))
#Output
#split1: ('/Users/gulanurmatova/Documents/UNH/Python/git/lecture4', 'homework')
#split2: ('/Users/gulanurmatova/Documents/UNH/Python/git/lecture4/homework', 'data_load.py')

#os.path.splitdrive - splits the path to passed file/directory to drive and the filepath/directorypath
#for the systems that do not use drives, like Linux, OSX, drive is returned as empty string
print("splitdrive1:",os.path.splitdrive(homework_dir_path))
print("splitdrive2:",os.path.splitdrive(homework_file_path))
#Output
#splitdrive1: ('', '/Users/gulanurmatova/Documents/UNH/Python/git/lecture4/homework')
#splitdrive2: ('', '/Users/gulanurmatova/Documents/UNH/Python/git/lecture4/homework/data_load.py')


#os.path.splitext - splits the path to passed file/directory to path and extension
#directory extensions are returned as an empty string
print("splitext1:",os.path.splitext(homework_dir_path))
print("splitext2:",os.path.splitext(homework_file_path))
#Output
#splitext1: ('/Users/gulanurmatova/Documents/UNH/Python/git/lecture4/homework', '')
#splitext2: ('/Users/gulanurmatova/Documents/UNH/Python/git/lecture4/homework/data_load', '.py')

#os.path.samefile - splits the path to passed file/directory from the file/directory
print("samefile:",os.path.samefile(homework_dir_path, symbolic_link+"/lecture4/homework"))
#Output
#samefile: True

#os.path.samefile - splits the path to passed file/directory from the file/directory
print("isabs1",os.path.isabs(homework_dir_path))
print("isabs2",os.path.isabs("./homework"))
#Output
#isabs1 True
#isabs2 False