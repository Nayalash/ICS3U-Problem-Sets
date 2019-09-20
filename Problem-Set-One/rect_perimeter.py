# Author: Nayalash Mohammad
# Date: September 19 2019
# File Name: rect_perimeter.py
# Description: A program that computes the perimeter of a rectangle based on the base and height.

def calculateRectanglePerimeter():

    # Get height and width inputs from user
    height = input("What is the height of your rectangle? (in meters)")
    width = input("What is the width of your rectangle? (in meters)")


    try:
        # Use Perimeter Formula for rectangle (P = 2H + 2W)
        calculation = (2 * float(height)) + (2 * float(width))

        print("The perimeter of the rectangle is: " + str(calculation) + " meters")

        # If there is an error (invalid value), print message to user.
    except ValueError:
        print("Sorry Invalid Number")


#Invoke Method
calculateRectanglePerimeter()
