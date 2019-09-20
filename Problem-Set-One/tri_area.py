# Author: Nayalash Mohammad
# Date: September 19 2019
# File Name: tri_area.py
# Description: A program that computes the area of a triangle based on the base and height.


def calculateTriangleArea():

    # Get height and width inputs from user
    height = input("What is the height of your triangle? (in meters)")
    width = input("What is the width of your triangle? (in meters)")


    try:
        # Use Area Formula for triangle (A = (Base * Height) / 2)
        calculation = (float(height) * float(width)) / 2

        print("The area of the triangle is: " + str(calculation) + " meters squared")

        # If there is an error (invalid value), print message to user.
    except ValueError:
        print("Sorry Invalid Number")


#Invoke Method
calculateTriangleArea()
