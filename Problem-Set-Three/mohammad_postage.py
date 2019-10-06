# Author: Nayalash Mohammad
# Date: October 5 2019
# File Name: postage.py
# Description: A program that tells the user the price of postage
# for a package based on weight.

# Ask the user for the weight of their package
weight = int(input("What is the weight of your letter in grams: "))

# Start out the cost variable to be zero
cost = 0

# Implement the test cases
if (weight < 30):
    cost = 48

elif (31 < weight < 50):
    cost = 70

elif (51 < weight <= 100):
    cost = 90

elif (weight > 100):
    # For Every 50 grams add 18 cents
    weight -= 100
    cost = 90 + (18 * (weight // 50))

# Display final price to user
print("Price of postage is: " + str(cost) + " cents.")