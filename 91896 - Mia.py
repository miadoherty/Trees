# importing libraries to be used
import time
import math

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
        intro()
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
    print("This is how it works: ")
    time.sleep(1)
    print("Starting in the tundra and working your way to the desert "
          "you will replant the plants around the world. ")
    time.sleep(1.5)
    print("You will start with $1 in your pocket. ")
    time.sleep(1)
    print("As you make more money, you will be able to unlock new vegetation "
          "to plant, ")
    time.sleep(1)
    print(" and eventually even have enough money to move into the next biome. ")
    time.sleep(2)
    print("Type end game at any time to end the game. ")
    time.sleep(1)
    instruct_choice()


# takes input from user
def instruct_choice():
    choice = str(input("Do you understand? ")).lower()
    if choice == "yes":
        print("Loading game... ")
        time.sleep(2)
    elif choice == "no":
        print("Alright... One more time. ")
        instruct()
    elif choice == "end game":
        x = exit()
        if x == "Y":
            quit()
        else:
            instruct_choice()
    else:
        error()
        instruct_choice()


# function prints the introduction
def intro():
    print("Greetings weary traveller. ")
    time.sleep(1.5)
    print("It may or may not come as a surprise to you that... ")
    time.sleep(1)
    print("the world has been ruined. ")
    time.sleep(1)
    print("For undisclosed reasons, it is now your "
          "responsibility to revive earth to its former glory. ")
    time.sleep(2)
    print("You are going to travel through the various biomes of Earth, ")
    time.sleep(1)
    print("simultaneously reviving and learning about the plant life. ")
    time.sleep(2)
    print("I wish you the best of luck. ")
    time.sleep(1.5)
    print("The fate of humanity is in your hands. ")
    time.sleep(2)
    choice = str(input("Are you ready to play? ")).lower()
    if choice == "yes":
        print("The game starts now. ")
    elif choice == "no":
        print("The game does not start now. ")
    elif choice == "end game":
        x = exit()
        if x == "Y":
            quit()
        else:
            intro()
    else:
        error()
        intro()


def undra():
    print("Introduce the tundra ")
    undra_value = 0
    undra_profit = 0
    undra_cost = 0
    while undra_profit < 100:
        if True:
            print("Would you like to plant a tree for: ")
            choice = (input("${:.2f} ".format(undra_cost)))
            if choice == "yes":
                undra_cost = undra_value * 2
                undra_value += 1
                undra_profit = (undra_value ** 2) - (undra_cost)
                print("You have planted", undra_value, "trees. ")
                print("You currently have: ")
                print("${:.2f}".format(undra_profit))
            else:
                print("${:.2f}".format(undra_value))
    while undra_profit >= 100:
        if True:
            print("You have made $100. You may now plant the next plant. ")
            choice = (input("Plant tree? "))
            if choice == "yes":
                undra_value += 1
                undra_profit = (undra_value ** 3) - (undra_value * 3)
                print("${:.2f}".format(undra_profit))
            else:
                print("No ")
    while undra_profit == 1000:
        if True:
            print("You have made $1000. You may now plant the next plant. ")
            break
  
hello()
