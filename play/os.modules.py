import os

name = os.ctermid()
print(name)


name = os.environ['HOME']
print(name