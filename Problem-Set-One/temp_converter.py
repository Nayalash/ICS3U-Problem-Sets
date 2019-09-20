# Author: Nayalash Mohammad
# Date: September 19 2019
# File Name: temp_converter.py
# Description: A program that takes the temperature in fahrenheit and converts it into celsius

def temperatureConverter():

    # Get the fahrenheit input from the user
    fahrenheit = input("What is the temperature in fahrenheit?")

    try:
        # Use Fahrenheit to Celsius Formula for the temperature (C = 5/9 * (F - 32))
        calculation = 5/9 * (float(fahrenheit) - 32)

        print("The temperature in celcius is: " + str(calculation) + " degrees")

        #BONUS: Rounding...

        print("The temperature in celcius is: " + str(round(int(calculation))) + " rounded degrees.")

        # If there is an error (invalid value), print message to user.
    except ValueError:
        print("Sorry Invalid Number")


#Invoke Method
temperatureConverter()