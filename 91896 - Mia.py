# importing libraries to be used
import time
import math


# valid answers
valid_answers = ["a", "b", "c", "end game"]


# checks answers and makes sure they are valid ^
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
    print("You buy trees to plant. ")
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
    print("the world has been ruined and our rainforests are no different. ")
    time.sleep(1)
    print("For undisclosed reasons, it is now your "
          "responsibility to revive the earth to its former glory. ")
    time.sleep(2)
    print("You are going to travel to the rainforest, ")
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
        print("loading... ")
        time.sleep(3)
        rainforest_text()
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


# function prints the rainforest text
def rainforest_text():
    time.sleep(2)
    print("A rainforest is a forest that is known for its high and continuous rainfall. ")
    time.sleep(1)
    print("Annual rainfall typically is between 2.5 metres and 4.5 metres. ")
    time.sleep(2)
    print("Though rainforests only cover about 6% of the Earth, "
          "they are home to more than half of the planets land animal species. ")
    time.sleep(2)
    print("Plants in tropical rainforests are extremely diverse. ")
    time.sleep(2)
    print("Within a 1-hectare plot of land, anywhere between 40 to 100 different species of tree can be found. ")
    time.sleep(2.5)
    print("The Amazon rainforest is the biggest deforestation front in the world. ")
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
        rainforest()
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


# runs the game 
def rainforest():
    # cost of each plant
    heliconia_cost = 1
    monkeybrush_cost = 10
    cacau_cost = 100
    # number of each plant
    rainforest_count = [0, 0, 0]    # [heliconia, monkeybrush, cacau]
    total_count = 0
    # profit from each plant
    total_profit = 1
    while total_profit <= 1000:
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
                    total_profit += add_rainforest(rainforest_count, heliconia_cost, monkeybrush_cost, cacau_cost)
                    heliconia_cost *= 1.4
                    print("You have planted heliconia flower ")
                    time.sleep(1)
                    print("")
                elif choice == "b" and total_profit >= monkeybrush_cost:
                    rainforest_count[1] += 1
                    total_count = sum(rainforest_count)
                    total_profit -= monkeybrush_cost
                    total_profit += add_rainforest(rainforest_count, heliconia_cost, monkeybrush_cost, cacau_cost)
                    monkeybrush_cost *= 1.4
                    print("You have planted monkey brush vine ")
                    time.sleep(1)
                    print("")
                elif choice == "c" and total_profit >= cacau_cost:
                    rainforest_count[2] += 1
                    total_count = sum(rainforest_count)
                    total_profit -= cacau_cost
                    total_profit += add_rainforest(rainforest_count, heliconia_cost, monkeybrush_cost, cacau_cost)
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
        if total_profit >= 1000:
            print("Congratulations! ")
            time.sleep(1)
            print("You have made: ")
            print("${:.2f}".format(total_profit))
            donation()


# the total profit made  
def add_rainforest(rainforest_count, heliconia_cost, monkeybrush_cost, cacau_cost):
    return 1 + (rainforest_count[0] * heliconia_cost) + (rainforest_count[1] * monkeybrush_cost) + (rainforest_count[2] * cacau_cost)


# takes input from user
def donation():
    choice = str(input("Would you like to donate all your profits to efforts to sustain the rainforest? "))
    if choice == "yes":
        print("That is very kind of you. ")
        print("loading... ")
        time.sleep(3)
        conclusion()
    elif choice == "no":
        print("Um... okay. ")
        print("loading...")
        time.sleep(3)
        conclusion()
    elif choice == "end game":
        x = exit()
        if x == "Y":
            quit()
    else:
        donation()


# prints the conclusion with facts
def conclusion():
    print("")
    print("Rainforests play an important part in our day to day life. ")
    time.sleep(2)
    print("The Amazon rainforest alone produces about 20% of the world's oxygen. ")
    time.sleep(2)
    print("The Amazon rainforest is the biggest deforestation front in the world. ")
    time.sleep(2)
    print("It is estimated by WWF about 27% of the Amazon biome will be without trees "
          "by 2030, if deforestation continues at its current rate. ")
    time.sleep(2)
    print("It is important that we look after the rainforests, and the animals in it. ")
    time.sleep(2)
    goodbye()


# says goodbye to user and ends the game.
def goodbye():
    print("Thank you for playing ")
    print("Stay icy. ")


hello()
