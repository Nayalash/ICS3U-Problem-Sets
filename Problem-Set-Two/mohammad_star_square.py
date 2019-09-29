# Author: Nayalash Mohammad
# Date: September 25 2019
# File Name: star_square.py
# Description: A program that asks a user for a number, 
# and prints that many '*' in user entered number of rows and columns.

# Ask user for a number
number = int(input("Enter a number: "))

for i in range(number): # Vertical

     for i in range(number):
          print('*', end=' ') # Horizontal

     print(' ') # So * can be spaced out
    