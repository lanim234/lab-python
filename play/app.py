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
        new_name = input("We are sorry about that. What is your name again? ")
        print("Welcome,", new_name)


checkName("Lanim")