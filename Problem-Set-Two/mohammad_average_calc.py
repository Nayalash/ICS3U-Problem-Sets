# Author: Nayalash Mohammad
# Date: September 25 2019
# File Name: average_calc.py
# Description: A program that asks a user for a number
# of grades, and computes the average of all the grades that
# the user will enter.

# Ask User for how many grades they want to enter
try:
     numberOfGrades = int(input("How Many Grades Do You Want To Enter?: "))

     grades = [] # Array (List), that holds all of the grades

     for i in range(numberOfGrades):
          mark = int(input("Enter Grade: ")) # Ask For A Mark, for the amount of times the user wants
          grades.append(mark) # Store the mark in the List (Array)

     gradeAverage = sum(grades) / numberOfGrades # Use Average Formula(A = (sumOfNumbers) / (numberOfNumbers))

     print(f"""The Average of the grades you entered is {gradeAverage} """)
except ValueError:
     print("Invalid Value")

