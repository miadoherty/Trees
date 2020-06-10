valid_answers = ["a", "b", "c"]


# function checks answers and makes sure they are valid ^
def checker(choice):
    if choice in valid_answers:
        return True
    else:
        print("Invalid choice, try again: ")
        return False


# function to end game at any time
def end():
    print("Are you sure you want to end the game? ")
    choice = str(input("Enter yes or no: ")).lower()
    if choice == "yes":
        print("Thanks for playing. ")
    elif choice == "no":
        print("alrighty")
    else:
        print("Invalid answer, please try again. ")
        end()

end()

