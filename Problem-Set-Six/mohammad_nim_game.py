# Author: Nayalash Mohammad
# Date: October 28 2019
# File Name: nim_game.py
# Description: A program that follows the game of nim algorithm

import random

gameOn = True
stoneAmount = random.randint(15, 30)
playerTurn = True
invalidTurn = False

while gameOn:
    if(not invalidTurn):
        print("There are currently " + str(stoneAmount) + " stones.")
    if(playerTurn):
        stonePick = int(input("How many stones would you like to take?: "))
        if(stonePick > 3 or stonePick < 1 or (stonePick > 2 and stoneAmount < 3)):
            invalidTurn = True
            print("You can not take that many stones!")
            continue
        stoneAmount -= stonePick
        print("You lifted " + str(stonePick) + " stones")
        invalidTurn = False
        playerTurn = False
    else:
        stonePick = random.randint(1, 2 if stoneAmount < 3 else 3)
        stoneAmount -= stonePick
        print("The computer has lifted " + str(stonePick) + " stones")
        playerTurn = True
    if stoneAmount < 2:
        gameOn = False
        if playerTurn:
            if stoneAmount == 0:
                print("The computer took the last stone. You won!")
            else:
                print("Uh oh, you must take the last stone. You lost!")
        else:
            if stoneAmount == 0:
                print("It seems like you took the last stone by accident... you lost.")
            else:
                print("Congrats. The computer must take the last stone. You won!")