# Author: Nayalash Mohammad
# Date: September 20 2019
# File Name: change_change.py
# Description: A program that tells the cashier how to pay an amount of change (< 0.99) back to the customer, in the form of coins


# Ask user for input
changeAmount = float(input("Enter a Amount of change less than 0.99 cents. For example: change = 0.87 ===> "))

# Keep Dividing and Subtracting until remainder is zero
quarters = changeAmount // 0.25
print("Number of quarters needed are: " + str(quarters))

qVal = quarters * 0.25
changeAmount = changeAmount - qVal

dimes = changeAmount // 0.1
print("Number of dimes needed are: " + str(dimes))

dVal = dimes * 0.1
changeAmount = round(changeAmount - dVal, 2) # Reason for rounding, as python is showing incorrect subtraction.

nickels = changeAmount // 0.05
print("Number of nickels need are: " + str(nickels))

nVal = nickels * 0.05
changeAmount = changeAmount - nVal

pennies = changeAmount // 0.01
print("Number of pennies needed are: " + str(pennies))

