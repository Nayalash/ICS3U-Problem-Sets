# Author: Nayalash Mohammad
# Date: October 5 2019
# File Name: postage.py
# Description: A program that tells the user the price of postage
# for a package based on weight.

# DOCUMENTATION ON README FILE, CALLED "postage_README.txt"

print("Welcome to Postage Price Calculator\nTo run the app, press r, to quit the app press q, for help press h \n")

def mainComputation():
    # Ask the user for the weight of their package
    weight = int(input("What is the weight of your letter in grams: "))

    # Start out the cost variable to be zero
    cost = 0

    # Implement the test cases
    if (weight <= 30):
        cost = 48

    elif (31 < weight < 50):
        cost = 70

    elif (51 < weight <= 100):
        cost = 90

    elif (weight > 100):
        # For Every 50 grams add 18 cents
        weight -= 100
        cost = 90 + (18 * (weight // 50))

    # Display final price to user
    print("Price of postage is: " + str(cost) + " cents. \nTo run again press `r`, to quit press `q`, for help press `h`")

def menu():
    run = input()

    # Menu Options
    if (run == "r") :
        mainComputation()
        menu()

    elif (run == 'q'):
        exit()
        menu()

    elif (run == 'h'):
        print("To Learn More About This Application. Visit the mohammad_postage_README.txt file.")
        print("To run the app, press r, to quit the app press q, for help press h")
        menu()

    else:
        print("Invalid Input, try running command `h`, for more details")
        menu()

# Initiate Program
menu()
