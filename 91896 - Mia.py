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
        print("loading... ")
        time.sleep(2)
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


def instruct_choice():
    choice = str(input("Do you understand? ")).lower()
    if choice == "yes":
        intro()
    elif choice == "no":
        print("Alright... One more time. ")
        instruct_choice()
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
    intro_choice()


# asks user if they are ready to play
def intro_choice():
    choice = str(input("Are you ready to play? ")).lower()
    if choice == "yes":
        print("The game starts now. ")
        tundra_text()
    elif choice == "no":
        print("Okay. I will ask you again in five seconds. ")
        time.sleep(5)
        intro_choice()
    elif choice == "end game":
        x = exit()
        if x == "Y":
            quit()
        else:
            intro()
    else:
        error()
        intro()


def tundra_text():
    print("Brrr... It sure is cold in the tundra. ")
    time.sleep(1)
    print("Maybe I should have worn socks. ")


def tundra():
    tundra_value = 1
    tundra_profit = 0
    tundra_cost = 0    
    while tundra_profit <= 100:
        print("Would you like to plant a tree for: ")
        choice = (input("${:.2f} ".format(tundra_cost)))
        if choice == "yes":
            tundra_cost = tundra_value * 2
            tundra_value += 1
            tundra_profit = (tundra_value ** 2) - (tundra_cost)
            print("You have planted", tundra_value, "trees. ")
            print("You currently have: ")
            print("${:.2f}".format(tundra_profit))
            time.sleep(1)
        else:
            error()
    while 100 < tundra_profit < 1000:
        if True:
            print("You have made $100. You may now plant the next plant. ")
            choice = (input("Plant tree? "))
            if choice == "yes":
                tundra_cost = tundra_value ** 2
                tundra_value += 1
                tundra_profit = 2 * (tundra_value ** 2) - (tundra_cost)
                print("${:.2f}".format(tundra_profit))
                time.sleep(1)
            else:
                error()
    if tundra_profit >= 1000:
        print("You have made $1000")


hello()