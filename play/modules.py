import os

name = os.uname()
print(name)

name = os.ctermid()
print(name)

name = os.environ["HOME"]
print(name)

name = geteuid()
print(name)
