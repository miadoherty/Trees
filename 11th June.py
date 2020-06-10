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
def end():
    print("Are you sure you want to end the game? ")
    choice = str(input("Enter yes or no: ")).lower()
    if choice == "yes":
        print("Thanks for playing. ")
    elif choice == "no":
        print("alrighty")
    else:
        error()
        end()


# function prints instructions
def hello():
    choice = str(input("Howdy partner! Is this your first rodeo? ")).lower()
    if choice == "yes":
        print("intro plays here. ")
    elif choice == "no":
        print("Alrighty. ")
    else:
        error()
        hello()


def instruct():
    print("It's pretty simple. Answer the questions with the corresponding lettter. ")