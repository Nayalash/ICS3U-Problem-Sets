# Author: Nayalash Mohammad
# Date: October 19 2019
# File Name: race.py
# Description: A program that uses the Tortoise and Hare Algorithm to simulate a race.

# Import Required Libraries
import random
import time

# Helper Function To Display Name and Progress
def display(name, progress):
    print(name + ": " + str(progress) + "/" + str(length))

# Ask user for length of the race
length = int(input("How long is this race? MIN = 20: "))

# Start Progress at zero
tortoiseProg = 0
hareProg = 0

# Initialize Moves Dictionaries
hareMoves = {0: 0, 1: 0, 2: 9, 3: 9, 4: -12, 5: 1, 6: 1, 7: 1, 8: -2, 9: -2}
tortoiseMoves = {0: 3, 1: 3, 2: 3, 3: 3, 4: 3, 5: -6, 6: -6, 7: 1, 8: 1, 9: 1}

# While Condition, Until Lengths are not less than zero
while hareProg < length or tortoiseProg < length:
    # Pick from the nine moves
    moveChoice = random.randint(0, 9)
    # Add moves to the progress counter
    tortoiseProg += tortoiseMoves[moveChoice]
    hareProg += hareMoves[moveChoice]

    if(tortoiseProg < 0):
        tortoiseProg = 0
    if(hareProg < 0):
        hareProg = 0

    # Display place every iteration
    if(hareProg < length and tortoiseProg < length):
        display("Tortoise", tortoiseProg)
        display("Hare", hareProg)
        time.sleep(0.5) # Slow Down Text Scrolling

# Display Outcome
if(hareProg == tortoiseProg):
    print("The Hare and the Tortoise have tied.")
elif(hareProg > tortoiseProg):
    print("The Hare has won!")
else:
    print("The Tortoise has won!")
