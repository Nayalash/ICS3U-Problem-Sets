# Author: Nayalash Mohammad
# Date: October 21 2019
# File Name: island_dice.py
# Description: A program that follows the island dice algorithm.

# Use random library to use randomint function
import random

# Starting number of shells
shells = 1000

def main(shells):

    while True:
        try:
            # Ask how many shells to risk
            riskAmount = int(input("How many shells would you like to risk?: "))
        except ValueError:
            print("Invalid Input")
            exit()

        # Check if user is not going over their total number of shells
        if riskAmount > shells:
            print("You don't have enough shells!")
            continue
        try:    
            # Ask them for high or low prediction
            bet = input("Do you predict a high or low number?\nTo bet High, type `high`. To bet Low, press any key...\n")
        except ValueError:
            print("Invalid Input")
            exit()

        betIsHigh = False

        if(bet.lower() == "high"):
            betIsHigh = True

        # Subtract by risked shells
        shells = shells - riskAmount
        # Combine two dice into one
        result = random.randint(1, 12)

        # Use Win-Lose Algorithm Provided
        if(result == 7):
            print("Rolled a total of 7. Better luck next time, you lost :(")
        elif(betIsHigh and result < 7 or not betIsHigh and result > 7):
            print("You rolled a total of " + str(result) + " which isn't in the range you predicted. Sorry, better luck next time.")
        else:
            # Double the shells
            shells = shells + ((riskAmount * 2))
            print("You rolled a total of " + str(result) + " which is in the range you predicted. Congrats.")

        # Print Shell Total
        print("Your shell total is: " + str(shells))

        # Prompt user for menu
        menu()


# Menu Method
def menu():
    print("To Run Program: type run, To Quit: type quit, For Help: type help")
    # Ask user for what they would like to do
    option = input()

    if (option == "run"):
        main(shells) # Run App
        menu()
    elif (option == "quit"):
        exit()
    elif (option == "help"):
        print('To run program, type `run` below, or `quit` to quit the program. Refer to docs for more info.')
        print('Type how many shells you want to risk, then enter if you predict a high or low number')
        menu()
    else:
        print("Invalid Input")
        menu()

# Init Program
print("Welcome To The Island Dice Game")
menu()