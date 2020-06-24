valid_answers = ["a", "b", "c"]


# function checks answers and makes sure they are valid ^
def checker(choice):
    if choice in valid_answers:
        return True
    else:
        print("Invalid choice, try again: ")
        return False


# function to display error message
def error():
    print("Invalid answer, please try again. ")


# function to end game at any time
def exit():
    value = " "
    choice = str(input("Are you sure you want to end the game? ")).lower()
    if choice == "yes":
        value = "Y"
    elif choice == "no":
        value = "N"
        print("Alright let's get right back to it. ")
    else:
        error()
        exit()
    return value


# function reads goodbye message to user
def quit():
    print("Thanks for playing :) ")


# function greets user
def hello():
    choice = str(input("Howdy partner! Is this your first rodeo? ")).lower()
    if choice == "yes":
        instruct()
    elif choice == "no":
        print("Intro plays here. ")
    elif choice == "end game":
        x = exit()
        if x == "Y":
            quit()
        else:
            hello()
    else:
        error()
        hello()


# function prints instructions
def instruct():
    print("It's pretty simple. ")
    print("Answer the questions with the corresponding letter. ")
    print("Type end game at any time to, you'll never guess, end the game. ")
    choice = str(input("Do you understand? ")).lower()
    if choice == "yes":
        print("intro plays here. ")
    elif choice == "no":
        print("Alright... One more time. ")
        instruct()
    elif choice == "end game":
        x = exit()
        if x == "Y":
            quit()
        else:
            instruct()
    else:
        error()
        instruct()


hello()
