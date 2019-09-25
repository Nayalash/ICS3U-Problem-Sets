# Author: Nayalash Mohammad
# Date: September 27 2019
# File Name: password_checker.py
# Description: A program that asks you for a master password,
# and allows you to keep trying the password until you get it right.

masterPassword = input("Enter Your Master Password: ")

password = None

while(masterPassword != password):
    password = input("Enter Password: ")

    while(masterPassword == password):
        print("You Have Guessed The Correct The Password")
        break


