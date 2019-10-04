# Author: Nayalash Mohammad
# Date: October 01 2019
# File Name: credit.py
# Description: A program that tells you your credit limit
# based on your questions answered

# Start the point balance with zero
points = 0

# Ask user questions, to determine eligibility of a credit card
age = int(input("What is your Age \n"))
yrsAtAddress = int(input("How many years have you been at your current address \n"))
income = int(input("What is your annual income \n"))
yrsAtJob = int(input("How many years have you been at your current job \n"))

# CategoryOne age
if (age < 20):
    score = -10
elif (21 < age < 30):
    score = 0
elif (31 < age < 50):
    score = 20
elif (age > 50):
    score = 25

# Store the points from the asked question
points = score

# CategoryTwo years at address
if (yrsAtAddress < 1):
    score = -5
elif (1 < yrsAtAddress < 3):
    score = 5
elif (4 < yrsAtAddress < 8):
    score = 12
elif (yrsAtAddress > 8):
    score = 20

# Store the points from the asked question
points = points + score

# CategoryThree income
if (income < 15000):
    score = 0
elif (income < 25000):
    score = 12
elif (income < 40000):
    score = 24
elif (income > 40000):
    score = 30

# Store the points from the asked question
points = points + score

# CategoryFour years at job
if (yrsAtJob < 2):
    score = -4
elif (2 < yrsAtJob < 4 ):
    score = 8
elif (yrsAtJob > 4):
    score = 15

# Store the points from the asked question
points = points + score

# ACTIONS
if (points < 20):
    print('Sorry We Can Not Offer You A Credit Card')
elif (21 < points < 35):
    print("We Can Offer You A Card With $500 Limit")
elif (36 < points < 60):
    print("We Can Offer You A Card With $2000 Limit")
elif (points > 60):
    print("We Can Offer You A Card With $5000 Limit")
