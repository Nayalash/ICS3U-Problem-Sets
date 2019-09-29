# Author: Nayalash Mohammad
# Date: October 01 2019
# File Name: leap_year.py
# Description: A program that asks a user for a year,
# that tells if a year is a leap year or not.

try:
    year = int(input("Enter a year: "))
except ValueError:
    print("Invalid Input")

if (year % 4) == 0:

    # Step 2
    if (year % 100) == 0:

        # Step 3
        if (year % 400) == 0:

            # Step 4
            print("This year is a leap year")

        else:
            # Step 5
            print("This year is not a leap year")

    else:
        # Step 4
        print("This year is a leap year")

else:
    # Step 5
    print("This year is not a leap year")


