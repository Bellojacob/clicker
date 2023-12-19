def clicker():
    i = 0
    while (True):
        userInput = input("Hello enter 1 to add one to clicker. Enter anything else to break.")
        if userInput == "1":
            i+=1
        else:
            break
    print("You entered 1 ",  i,  " times")
        
clicker()
        