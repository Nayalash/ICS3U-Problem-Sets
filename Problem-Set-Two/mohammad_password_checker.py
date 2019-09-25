# Author: Nayalash Mohammad
# Date: September 27 2019
# File Name: password_checker.py
# Description: A program that asks you for a master password,
# and allows you to keep trying the password until you get it right.

# Ask user for the password they are trying to guess
masterPassword = input("Enter Your Master Password: ")

# Set passeword equal to None (NULL) for place holder reasons
password = None

# Check if user entered the right password
while(masterPassword != password):
    password = input("Enter Password: ")

    # When user enters correct password, print something
    while(masterPassword == password):
        print("You Have Guessed The Correct The Password")
        break # Use break, so message does not print repeatedly


