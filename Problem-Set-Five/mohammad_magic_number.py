# Author: Nayalash Mohammad
# Date: October 20 2019
# File Name: magic_number.py
# Description: A program that generates a number between 1 - 10, and allows the user to guess it.

# Import random library to use random function
import random

# Main Method
def main():
    randomNumber = random.randint(1,10)
    # print(randomNumber)

    # Start guess and counter with 0
    guess = 0
    i = 0

    # Activate loop when guess does not equal to random number
    while(randomNumber != guess):
        # Ask for guess
        guess = int(input("Enter Guess Between 1-10, to quit type `11` as your guess\n"))
        # Add to attempt count
        i = i + 1

        # Win Output
        if (randomNumber == guess):
            print("******************")
            print("You Win")
            print("Number was : " + str(randomNumber))
            print("Attempts: " + str(i))
            print("To Run again, type run")
            break

        # Lose Output
        elif (guess == 11):
            print("******************")
            print("You Lose")
            print("Number was : " + str(randomNumber))
            print("Attempts: " + str(i))
            print("To Run again, type run")
            break

# Menu Method
def menu():
    # Ask user for what they would like to do
    option = input()

    if (option == "run"):
        main() # Run App
        menu()
    elif (option == "quit"):
        exit()
    elif (option == "help"):
        print('To run program, type `run` below, or `quit` to quit the program. Refer to docs for more info.')
        print('When you have ran the program, keep trying to guess the number between 1-10, if you give up type 11 as your guess')
        menu()
    else:
        print("Invalid Input")
        menu()

# Init Program
print("Welcome To The Magic Number Game \nTo Run Program: type run, To Quit: type quit, For Help: type help\n")
menu()