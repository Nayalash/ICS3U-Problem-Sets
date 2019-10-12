# Name: Nayalash Mohammad
# Date: October 12 2019
# File Name: necklace.py
# Description: A program that follows the necklace algorithm

# Import Module Time
import time

# Ask user for number
number = int(input("Input a number: "))

# Put it in a loop so chain never breaks
while (True):

    print(int(number))

    # Follow Problem Set Guidelines
    if(number % 2 == 0):
        number = number / 2
    else:
        number = 3 * number + 1

    # Show iterations happening slowly
    time.sleep(0.50)