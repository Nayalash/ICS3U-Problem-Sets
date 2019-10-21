# Author: Nayalash Mohammad
# Date: October 21 2019
# File Name: coin_toss.py
# Description: A program that allows the user to toss a coin, and displays tosses vs counter ratio.

# Initialize random library, to use random integer function
import random

# Start counters and tosses with zero
counter = 0
i = 0

# Have a break/ run case for the loop
run = True

while (run):
    # Ask user to flip
    flip = input("To Flip Press `r' to stop flipping press `q`")
    # Increase Toss Counter
    i = i + 1
    # Random Toss
    headOrTail = random.randint(1,2)

    # Coin Toss Algorithm
    if (flip == "r"):
        # 1 is Head
        if (headOrTail == 1):
            print("HEAD")
            counter = counter + 1
        # 2 is Tail
        elif(headOrTail == 2):
            print("TAIL")
            counter = counter - 1
            
    elif (flip == "q"):
        # Break out of loop
        run = False
        print("Total Flips: " + str(i - 1))
        print("Counter : " + str(counter))

    else:
        print("Invalid Input")
