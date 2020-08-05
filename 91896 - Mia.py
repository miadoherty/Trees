# importing libraries to be used
import time
import math

valid_answers = ["a", "b", "c", "end game"]


# function checks answers and makes sure they are valid ^
def checker(choice):
    if choice in valid_answers:
        return True
    else:
        print("")
        print("Invalid answer, try again: ")
        return False


# function to display error message
def error():
    print("Invalid answer, try again: ")
    print("")


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
    print("The more trees you have, the more money you make from resources ")
    time.sleep(1)
    print("As you make more money, you will be able to unlock new vegetation "
          "to plant, ")
    time.sleep(1)
    print(" and eventually even have enough money to move into the next biome. ")
    time.sleep(2)
    print("Type end game at any time to end the game. ")
    time.sleep(1)
    instruct_choice()


# function takes input from user to check they understand
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
    print("loading... ")
    time.sleep(2)
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


# function takes input from user to check they are ready to play
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
        intro_choice()


# function prints the tundra text
def tundra_text():
    time.sleep(2)
    print("Brrr... It sure is cold in the tundra. ")
    time.sleep(1)
    print("Maybe I should have worn socks. ")
    time.sleep(2)
    print("While we are here, "
          "why don't I tell you some fun facts about the tundra. ")
    time.sleep(2)
    print("Did you know that the word 'tundra' comes from the Finnish "
          "word 'tunturia', which means barren or treeless hill. ")
    time.sleep(2)
    print("Rather than big trees, the tundra has patchy vegetation "
          "that tends to be low to the ground. ")
    time.sleep(2)
    print("This usually consists of grasses, mosses, lichens, sedges and "
          "small shrubs. ")
    time.sleep(2)
    print("These kinds of plants are well adapted to withstand the harsh "
          "tundra conditions. ")
    time.sleep(2)
    print("Hey! ")
    time.sleep(1.5)
    print("What is that over there. ")
    time.sleep(1)
    print("It looks like a gold coin donation. ")
    time.sleep(1)
    coin()


# function ask if user wants to pick up the coin (must in order to move on with game)
def coin():
    choice = str(input("Do you want to pick up the coin? ")).lower()
    if choice == "yes":
        print("You have picked up the coin. ")
        print("Funnily enough $1 is just the right amount to plant a lucious bush. ")
        time.sleep(1)
        print("")
        tundra()
    elif choice == "no":
        print("I strongly suggest you pick up the coin. ")
        coin()
    elif choice == "end game":
        x = exit()
        if x == "Y":
            quit()
        else:
            coin()
    else:
        error()
        coin()


# 
def tundra():
    # cost of each plant
    bearberry_cost = 1
    articmoss_cost = 10
    saxifrage_cost = 100
    # number of each plant
    tundra_count = [0,0,0]    #[bearberry, articmoss, saxifrage]
    # profit from each plant
    tundra_profit = [0, 0, 0]
    while tundra_profit <= 1000:
        if tundra_profit >= bearberry_cost or tundra_profit >= articmoss_cost or tundra_profit >= saxifrage_cost:
            print("You currently have: ")
            print("${:.2f}".format(tundra_profit))
            print("Do you want to plant? ")
            print("A) A bearberry shrub for ")
            print("${:.2f}".format(bearberry_cost))
            print("B) Artic moss for ")
            print("${:.2f} ".format(articmoss_cost))
            print("C) Tufted Saxifrage for ")
            print("${:.2f} ".format(saxifrage_cost))
            choice = str(input("")).lower()
            if checker(choice) is True:
                if choice == "a" and tundra_profit >= bearberry_cost:
                    bearberry_count += 1
                    bearberry_cost *= 1.2
                    bearberry_profit = 2 + bearberry_count ** 2
                    tundra_count = bearberry_count + articmoss_count + saxifrage_count
                    tundra_profit = (bearberry_profit + articmoss_profit + saxifrage_profit) - bearberry_cost
                    print("You have planted bearberry shrub ")
                    print("You have planted", tundra_count, "trees. ")
                    time.sleep(1)
                    print("")
                elif choice == "b" and tundra_profit >= articmoss_cost:
                    articmoss_count += 1
                    articmoss_cost *= 1.2
                    articmoss_profit = 4 + articmoss_count ** 2
                    tundra_count = bearberry_count + articmoss_count + saxifrage_count
                    tundra_profit += (bearberry_profit + articmoss_profit + saxifrage_profit) - articmoss_cost
                    print("You have planted artic moss ")
                    print("You have planted", tundra_count, "trees. ")
                    time.sleep(1)
                    print("")
                elif choice == "c" and tundra_profit >= saxifrage_cost:
                    saxifrage_count += 1
                    saxifrage_cost *= 1.2
                    saxifrage_profit = 6 + saxifrage_count ** 2
                    tundra_count = bearberry_count + articmoss_count + saxifrage_count
                    tundra_profit += (bearberry_profit + articmoss_profit + saxifrage_profit) - saxifrage_cost
                    print("You have planted tufted saxifrage ")
                    print("You have planted", tundra_count, "trees. ")
                    time.sleep(1)
                    print("")
                elif choice == "end game":
                    x = exit()
                    if x == "Y":
                        quit()
                        break
                else:
                    print("Sorry you have insufficent funds. ")
                    time.sleep(1)
    if tundra_profit >= 1000:
        print("You have made a grand total of: ")
        print("${:.2f}".format(tundra_profit))
        tundra_choice()


def tundra_choice():
    print("")
    print("loading... ")
    time.sleep(3)
    print("Wow you made so much money from planting plant and harvesting the resources, sustainably. ")
    print("You only need $500 to move on to the next biome and buy your next plant. ")
    time.sleep(1)
    choice = str(input("The rest your money will  "))
    if choice == "yes":
        rainforest_text()
    elif choice == "end game":
        x = exit()
        if x == "Y":
            quit()
        else:
            tundra_choice()


def rainforest_text():
    time.sleep(2)
    print("yes")


def rainforest():
    # cost of each plant
    heliconia_cost = 10
    monkeybrush_cost = 100
    cacau_cost = 1000
    # number of each plant
    rainforest_count = [0, 0, 0]    # [heliconia, monkeybrush, cacau]
    total_count = 0
    # profit from each plant     
    total_profit = 10
    while total_profit <= 10000:
        if total_profit >= heliconia_cost or total_profit >= monkeybrush_cost or total_profit >= cacau_cost:
            print("")
            print("You have planted: ")
            print(rainforest_count[0], "heliconia flowers ")
            print(rainforest_count[1], "monkey brush vines ")
            print(rainforest_count[2], "cacau trees ")
            print("You currently have: ")
            print("${:.2f}".format(total_profit))
            print("")
            print("Do you want to plant? ")
            print("A) A heliconia flower for ")
            print("${:.2f}".format(heliconia_cost))
            print("B) A monkey brush vine for ")
            print("${:.2f} ".format(monkeybrush_cost))
            print("C) A cacau tree for ")
            print("${:.2f} ".format(cacau_cost))
            choice = str(input("")).lower()
            if checker(choice) is True:
                if choice == "a" and total_profit >= heliconia_cost:
                    rainforest_count[0] += 1
                    total_count = sum(rainforest_count)
                    total_profit -= heliconia_cost
                    total_profit = 15 + rainforest_count[0] ** 3
                    heliconia_cost *= 1.4
                    print("You have planted heliconia flower ")
                    time.sleep(1)
                    print("")
                elif choice == "b" and total_profit >= monkeybrush_cost:
                    rainforest_count[1] += 1
                    total_count = sum(rainforest_count)
                    total_profit -= monkeybrush_cost
                    total_profit = 150 + total_count ** 3
                    monkeybrush_cost *= 1.4
                    print("You have planted monkey brush vine ")
                    print(rainforest_count)
                    time.sleep(1)
                    print("")
                elif choice == "c" and total_profit >= cacau_cost:
                    rainforest_count[2] += 1
                    total_count = sum(rainforest_count)
                    total_profit -= cacau_cost
                    total_profit = 1500 + total_count ** 3
                    cacau_cost *= 1.4
                    print("You have planted cacau tree ")
                    time.sleep(1)
                    print("")
                elif choice == "end game":
                    x = exit()
                    if x == "Y":
                        quit()
                else:
                    print("Sorry you have insufficent funds. ")
                    time.sleep(1)


rainforest()