# Author: Nayalash Mohammad
# Date: September 20 2019
# File Name: easter_calc.py
# Description: A program that calculates when easter is, depending on a year inputted


try:

    # Ask for year input from user
    year = int(input("ENTER A YEAR ! : "))

    # Easter Formula
    a = year % 9
    b = year / 10
    c = year % 100
    d = b / 4
    e = b % 4
    f = ((8 * b) + 13) / 25
    g = ((19 * a) + b - d - f + 15) % 30
    h = (a + (11 * g)) / 319
    i = c / 4
    j = c % 4
    m = ((2 * e) + (2 * i) - g - h - j + 32) % 7

    month = round((g - h + m + 90) / 25)
    day = round((g - h + m + month + 19) % 32)


    if month == 2 or 3:
        month = "March"
    elif month == 4 or 5:
        month = "April"

    print(f"""Easter is on {month}, {day} in the year: {year}""")

except ValueError:
    print("Invalid Year")