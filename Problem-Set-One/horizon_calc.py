# Author: Nayalash Mohammad
# Date: September 20 2019
# File Name: horizon_calc.py
# Description: A program that calculates your distance to the horizon

import math

def calculateDistanceToHorizon():

    try:
        # Get distance and time inputs from user
        height = float(input("What is the height from the ground (in centimeters)"))
        # Use Distance Formula for the baseball (D = sqrt(0.126 * H))
        calculation = (math.sqrt(0.126 * height)) / 10000


        print("The distance to horizon is : " + str(calculation) + " km")

        # If there is an error (invalid value), print message to user.
    except ValueError:
        print("Sorry Invalid Number")


#Invoke Method
calculateDistanceToHorizon()

