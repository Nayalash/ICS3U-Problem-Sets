# Author: Nayalash Mohammad
# Date: October 28 2019
# File Name: nim_game.py
# Description: A program that follows the game of nim algorithm

# Import Random Library, to use RandInt Function
import random


def main():
    # Have a condition for the app to start
    gameOn = True
    # Generate Random Stone Amount
    stoneAmount = random.randint(15, 30)

    # Set constraints for inputs by user
    playerTurn = True
    invalidTurn = False

    while gameOn:

        if(not invalidTurn):
            # Show Starting number of stones
            print("There are currently " + str(stoneAmount) + " stones.")

        if(playerTurn):
            try:
                # Ask for how many stones to take
                stonePick = int(input("How many stones would you like to take?: "))
            except ValueError:
                print("Invalid Input")
                exit()

            # Verify that those amount of stones can be taken
            if(stonePick > 3 or stonePick < 1 or (stonePick > 2 and stoneAmount < 3)):
                invalidTurn = True
                print("You can not take that many stones!")
                continue

            # Subtract by total stones taken    
            stoneAmount -= stonePick

            print("You lifted " + str(stonePick) + " stones")

            # Re-Evaluate program constraints
            invalidTurn = False
            playerTurn = False

        else:
            # Make sure stones can be taken
            stonePick = random.randint(1, 2 if stoneAmount < 3 else 3)
            stoneAmount -= stonePick
            print("The computer has lifted " + str(stonePick) + " stones")
            playerTurn = True

        if stoneAmount < 2:

            # Exit Program
            gameOn = False

            # Print Who Won
            if playerTurn:
                if stoneAmount == 0:
                    print("The computer took the last stone. You won!")
                else:
                    print("Uh oh, you must take the last stone. You lost!")
            else:
                if stoneAmount == 0:
                    print("It seems like you took the last stone by accident... you lost.")
                else:
                    print("Congrats. The computer must take the last stone. You won!")

    menu()


# Menu Method
def menu():
    print("To Run Program: type run, To Quit: type quit, For Help: type help")
    # Ask user for what they would like to do
    option = input()

    if (option == "run"):
        main() # Run App
        menu()
    elif (option == "quit"):
        exit()
    elif (option == "help"):
        print('To run program, type `run` below, or `quit` to quit the program. Refer to docs for more info.')
        print('Type how many stones you would like to take (1,2 or 3) until you or the computer takes the last shell')
        menu()
    else:
        print("Invalid Input")
        menu()

# Init Program
print("Welcome To The Game of Nim")
menu()