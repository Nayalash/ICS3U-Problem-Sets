# Author: Nayalash Mohammad
# Date: September 19 2019
# File Name: circumference_calc_ROUND.py
# Description: A program that calculates the circumference of a circle

# Import Math Library
import math

def calculateCircleCircumference():

    # Get the radius input from the user
    radius = input("What is the radius of your circle (in meters)")

    try:
        # Use Circumference Formula for the Circle (C = 2 * Pi * radius)
        calculation = 2 * math.pi * float(radius)

        print("The circumference of the circle is: " + str(calculation) + " meters")

        #BONUS: Rounding...

        print("The circumference of the circle is: " + str(round(calculation)) + " rounded meters.")

        # If there is an error (invalid value), print message to user.
    except ValueError:
        print("Sorry Invalid Number")


#Invoke Method
calculateCircleCircumference()