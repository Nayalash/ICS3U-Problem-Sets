# Author: Nayalash Mohammad
# Date: September 19 2019
# File Name: velocity_calc.py
# Description: A program that calculates the velocity of a baseball thrown in the air

def calculateBaseballVelocity():

    # Get distance and time inputs from user
    distance = input("What is the distance that your baseball reached (in meters)")
    seconds = input("What is the time it took your baseball to reach that distance? (in seconds)")

    try:
        # Use Velocity Formula for the baseball (Velocity = Distance / Time)
        calculation = float(distance) / float(seconds)

        print("The velocity of the baseball is: " + str(calculation) + " m/s")

        # If there is an error (invalid value), print message to user.
    except ValueError:
        print("Sorry Invalid Number")


#Invoke Method
calculateBaseballVelocity()
