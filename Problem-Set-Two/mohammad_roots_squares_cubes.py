# Author: Nayalash Mohammad
# Date: September 26 2019
# File Name: squares_roots_cubes.py
# Description: A program that asks a user for a range
# and prints the square, root and cube of all the numbers
#in that range.

import math # Import Math Library, to use square root function

# If user inputs not a integer, print something to console
try:
    # Ask user for a start and a stop
    start = int(input("Start: "))
    stop = int(input("Stop: "))

    print(">>>>>>>>>>>>>>>>>>>")
    print(">>>>>>>>>>>>>>>>>>>")

except ValueError:
    print("Invalid Value")

# Initialize For Loop, with a start and stop
for i in range(start, stop):

    # Define Formulas for finding squares, roots and cubes
    square = i * i
    root = math.sqrt(i)
    cube = i * i * i

    # Print Results to Console
    print("Number: " + str(i))
    print("Square: " + str(square))
    print("Root: " + str(root))
    print("Cube: " + str(cube))
    print("*******************")


