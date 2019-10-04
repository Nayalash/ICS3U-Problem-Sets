# Author: Nayalash Mohammad
# Date: October 01 2019
# File Name: zodiac.py
# Description: A program that displays your
# zodiac sign based on your birthday

# Ask user for their birthday
try:
    day = int(input("Enter Birth Day: "))
    month = int(input("Enter Month In Number Format (ex: September = 9) "))
except ValueError:
    print("Invalid Input")

# Use Zodiac Algorithm

if month == 12: # December
    if (day < 22):
        sign = 'Sagittarius'
    else:
        sign = 'Capricorn'

elif month == 1: # January
    if (day < 20):
        sign = 'Capricorn'
    else:
        sign = 'Aquarius'

elif month == 2: # February
    if (day < 19):
        sign = 'Aquarius'
    else:
        sign = 'Pisces'

elif month == 3: # March
    if (day < 21):
        sign = 'Pisces'
    else:
        sign = 'Aries'

elif month == 4: # April
    if (day < 20):
        sign = 'Aries'
    else:
        sign = 'Taurus'

elif month == 5: # May
    if (day < 21):
        sign = 'Taurus'
    else:
        sign = 'Gemini'

elif month == 6: # June
    if (day < 21):
        sign = 'Gemini'
    else :
        sign = 'Cancer'

elif month == 7: # July
    if (day < 23):
        sign = 'Cancer'
    else:
        sign = 'Leo'

elif month == 8: # August
    if (day < 23):
        sign = 'Leo'
    else:
        sign = 'Virgo'

elif month == 9: # September
    if (day < 23):
        sign = 'Virgo'
    else:
        sign = 'Libra'

elif month == 10: # October
    if (day < 23):
        sign = 'Libra'
    else:
        sign = 'Scorpio'

elif month == 11: # November
    if (day < 22):
        sign = 'Scorpio'
    else:
        sign = 'Sagittarius'

# Print the result to the console
print("The Astrological sign for your birthday is: " + sign)