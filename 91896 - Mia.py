# importing libraries to be used
import time
import math

valid_answers = ["a", "b", "c", "end game"]

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
    print("With more tree comes more resources "
          "which in turn can be sold for money. ")
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


def intro_choice():
    choice = str(input("Are you ready to play? ")).lower()
    if choice == "yes":
        print("loading... ")
        time.sleep(3)
        tundra_intro()
    elif choice == "no":
        print("Okay. I will ask you again in five seconds. ")
        time.sleep(5)
        intro_choice()
    elif choice == "end game":
        x = exit()
        if x == "Y":
            quit()
        else:
            intro_choice()
    else:
        error()
        intro_choice()


def tundra_intro():
    print("Brrr... It sure is cold in the tundra. ")
    time.sleep(1)
    print("Maybe I should have worn socks. ")
    time.sleep(1.5)
    print("While we are here, why don't I tell you some fun facts about the tundra. ")
    time.sleep(1.5)
    print("Did you know that the word 'tundra' comes from the Finnish word ' tunturia'. ")
    time.sleep(2)
    print("'Tunturia' means barren or treeless hill. ")
    time.sleep(2)
    print("Rather than big trees, the tundra has patchy vegetation "
          "that tends to be low to the ground. ")
    time.sleep(2)
    print("This usually consists of grasses, mosses, lichens, sedges and small shrubs. ")
    time.sleep(1.5)
    print("These kinds of plants are better adapted to withstand the harsh tundra conditions. ")
    time.sleep(3)
    print("Hey! ")
    time.sleep(1)
    print("What is that over there. ")
    time.sleep(1)
    print("It looks like a gold coin donataion. ")
    time.sleep(1)
    coin()


def coin():
    choice = str(input("Do you want to pick up the coin? ")).lower()
    if choice == "yes":
        print("You have picked up the coin. ")
    elif choice == "no":
        print("I strongly suggest you pick up the coin. ")
    elif choice == "end game":
        x = exit()
        if x == "Y":
            quit()
        else:
            coin()
    else:
        error()
        coin()


def undra():  
# cost of each plant
    bearberry_cost = 1
    articmoss_cost = 10
    saxifrage_cost = 100
# number of each plant
    bearberry_count = 0
    articmoss_count = 0
    saxifrage_count = 0
    undra_count = 0
# profit from each plant
    bearberry_profit = 0
    articmoss_profit = 0
    saxifrage_profit = 0
    undra_profit = 1
    while undra_profit <= 1000 and undra_count <= 50:
        if undra_profit >= bearberry_cost or undra_profit >= articmoss_cost or undra_profit >= saxifrage_cost:
            print("You currently have: ")
            print("${:.2f}".format(undra_profit))
            print("Do you want to plant? ")
            print("A) A bearberry shrub for ")
            print("${:.2f}".format(bearberry_cost))
            print("B) Artic moss for ")
            print("${:.2f} ".format(articmoss_cost))
            print("C) Tufted Saxifrage for ")
            print("${:.2f} ".format(saxifrage_cost))
            choice = str(input("")).lower()
            if checker(choice) == True:
                if choice == "a" and undra_profit >= bearberry_cost:
                    bearberry_count += 1
                    bearberry_cost *= 1.2
                    bearberry_profit = 2 + bearberry_count ** 2
                    undra_count = bearberry_count + articmoss_count + saxifrage_count
                    undra_profit = (bearberry_profit + articmoss_profit + saxifrage_profit) - bearberry_cost
                    print("You have planted bearberry shrub ")
                    print("You have planted", undra_count, "trees. ")
                    time.sleep(1)
                    print("")
                elif choice == "b" and undra_profit >= articmoss_cost:
                    articmoss_count += 1
                    articmoss_cost *= 1.2
                    articmoss_profit = 2 + articmoss_count ** 2
                    undra_count = bearberry_count + articmoss_count + saxifrage_count
                    undra_profit += (bearberry_profit + articmoss_profit + saxifrage_profit) - articmoss_cost
                    print("You have planted artic moss ")
                    print("You have planted", undra_count, "trees. ")
                    time.sleep(1)
                    print("")
                elif choice == "c" and undra_profit >+ saxifrage_cost:
                    saxifrage_count += 1
                    saxifrage_cost *= 1.2
                    saxifrage_profit = 2 + saxifrage_count ** 2 
                    undra_count = bearberry_count + articmoss_count + saxifrage_count
                    undra_profit += (bearberry_profit + articmoss_profit + saxifrage_profit) - saxifrage_cost
                    print("You have planted tufted saxifrage ")
                    print("You have planted", undra_count, "trees. ")
                    time.sleep(1)
                    print("")
                elif choice == "end game":
                    x = exit()
                    if x == "Y":
                        quit()
                    else:
                        undra()
                else:
                    print("Sorry you have insufficent funds. ")
                    time.sleep(1)
    print("You have made over ")
    print("${:.2f}".format(undra_profit))


undra()
