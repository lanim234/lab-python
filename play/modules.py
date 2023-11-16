import os

name = os.uname()
print(name)

name = os.ctermid()
print(name)

name = os.environ["HOME"]
print(name)

home1 = os.getenv("HOME", default="/")
print(home1)
