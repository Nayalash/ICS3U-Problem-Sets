# Name: Nayalash Mohammad
# Date: October 12 2019
# File Name: factorial.py
# Description: A program that computes the factorial for a number

number = int(input("Enter Number: "))

# Total number which will be incremented (multiplied) by every positive integer value above 0 and saved in the variable
total = 1

# Iterate through all numbers starting from 1 to the number itself
# (number + 1 since range function is excludes the upper bound value)
for curr in range(1, number + 1):
    # multiply the total by the current number and store the product as the new total
    total *= curr

# When the factorial is calculated, print it
print(total)
