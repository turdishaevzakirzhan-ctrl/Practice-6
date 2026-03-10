import os

os.mkdir("dir1")
print(os.listdir("."))

os.makedirs("a/b")
print(os.listdir("a"))

os.mkdir("test")
print(os.path.isdir("test"))

os.makedirs("x/y/z")
print(os.listdir("x"))

os.mkdir("folder5")
print(os.listdir("."))