# Author: Nayalash Mohammad
# Date: September 25 2019
# File Name: horizontal_stars.py
# Description: A program that asks a user for a number, 
# and prints that many '*' characters in a horizontal line.

# Ask user for a number
number = int(input("Enter a number: "))


for i in range(number):
    print('*', end='')