# Author: Nayalash Mohammad
# Date: September 27 2019
# File Name: what_number.py
# Description: A program that asks a user for a number,
# tells whether it is odd or even, or positive/negative/zero

# Ask user for a number
try:
    number = int(input("Enter a number: "))
except ValueError:
    print("Invalid Input (ONLY INTEGER TYPE IS ALLOWED)")

# Checking to see if it can be evenly divisible by two, making it even. If not it is odd.
if ((number % 2) == 0):
    print("This number is even...")
else:
    print("This number is odd...")

# Checking to see if it is negative, zero or positive
if number < 0:
    print("This number is also negative...")
elif number == 0:
    print("This number is also zero...")
else:
    print("This number is also positive...")


