name ="lanim"

if name== "kenzo":
    print('yes, my name is lanim')

else:
    print('oh! you got the name wrong')


def checkName(name):
    answer = input("Is your name " + name + "? ")
    if answer.lower() == "yes":
        print("Hello, ", name)
    else:
        print("We are sorry about that")


checkName("Lanim")