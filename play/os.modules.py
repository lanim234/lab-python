import os

name = os.ctermid()
print(name)


name = os.environ['HOME']
print(name)


name = os.getenv("HOME1", default=None)
print(name)