def sayHelloWorld(name):
    print("Hello world! ", name , ", nice to meet you.")

option = True    

while (option == True):
    name = input("What is your name? Insert q to close. ")
    if (name == "q"):
        option = False
    else:
        sayHelloWorld(name)
