import os

name = os.uname()
print(name)

name = os.ctermid()
print(name)

name = os.environ["HOME"]
print(name)

home1 = os.getenv("HOME", default="/")
print(home1)


with open("/tmp/1.txt", "w") as file:
    file.write("This is an example file\n")
    file.write("It was created using the OS module in python.")


command = "ls -l"

exit_status = os.system(command)

print(exit_status)

#if exit_status == 0:
#    print("Command executed successfully,")
#else:
#    print("Command execution failed")
