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


# function greets user
def hello():
    choice = str(input("Howdy partner! Is this your first rodeo? ")).lower()
    if choice == "yes":
        instruct()
    elif choice == "no":
        print("Intro plays here. ")
    else:
        error()
        hello()


# function prints instructions
def instruct():
    print("It's pretty simple. Answer the questions with the corresponding letter. ")
    print("Type end game at any time to, you'll never guess, end the game. ")
    choice = str(input("Do you understand? ")).lower()
    if choice == "yes":
        print("intro plays here. ")
    elif choice == "no":
        print("Alright... One more time. ")
        instruct()
    else:
        error()
        instruct()


# tracks number of trees in rainforest????????????????????????????
while rainforest < 100:
    print("You need to plant more trees. ")
    ra = raw_input("How many trees do you want to plant? ")


hello()