import os

print(os.getcwd())
print(os.listdir())
os.chdir("./homework")
print(os.getcwd())
os.chdir("..")
print(os.getcwd())
os.chdir(os.getcwd()+"/homework")
print(os.getcwd())