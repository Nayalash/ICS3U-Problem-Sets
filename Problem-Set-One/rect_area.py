# Author: Nayalash Mohammad
# Date: September 19 2019
# File Name: rect_area.py
# Description: A program that computes the area of a rectangle based on the height and width.


def calculateRectangleArea():

  # Get height and width inputs from user
  height = input("What is the height of your rectangle? (in meters)")
  width = input("What is the width of your rectangle? (in meters)")


  try:
    # Use Area Formula for rectangle (A = H * W)
    calculation = float(height) * float(width)

    print("The area of the rectangle is: " + str(calculation) + " meters squared")

    # If there is an error (invalid value), print message to user.  
  except ValueError:
    print("Sorry Invalid Number")


#Invoke Method
calculateRectangleArea()