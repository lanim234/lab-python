import os

name = os.ctermid()
print(name)


name = os.environ['HOME']
print(name)


name = os.getenv("centos", default=None)
print(name)

with open("/tmp/1.txt", "w") as file:
    file.write("This is an example file.\n")
    file.write("It was created using the os module in python.")