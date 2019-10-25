# Author: Nayalash Mohammad
# Date: October 21 2019
# File Name: island_dice.py
# Description: A program that follows the island dice algorithm.

import random

shells = 1000

while True:
    riskAmount = int(input("How many shells would you like to risk?: "))
    if riskAmount > shells:
        print("You don't have enough shells!")
        continue
    bet = input("Do you predict a high or low number?: ")
    betIsHigh = False
    if(bet.lower() == "high"):
        betIsHigh = True

    shells -= riskAmount
    result = random.randint(1, 12)

    if(result == 7):
        print("Rolled a total of 7. Better luck next time, you lost :(")
    elif(betIsHigh and result < 7 or not betIsHigh and result > 7):
        print("You rolled a total of " + str(result) + " which isn't in the range you predicted. Sorry, better luck next time.")
    else:
        shells += riskAmount * 2
        print("You rolled a total of " + str(result) + " which is in the range you predicted. Congrats.")
    print("Your shell total is: " + str(shells))