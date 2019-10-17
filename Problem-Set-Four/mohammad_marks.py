# Author: Nayalash Mohammad
# Date: October 15 2019
# File Name: marks.py
# Description: A program that inputs Grade Value and outputs class average
# along with passing and failing count


# Ask user for number of students in their class
students = int(input("How many students are in your class: "))

# Initialize an empty array for student marks
marks = []

# Start the passing/failing count at zero
passing = 0
failing = 0

# Ask the student marks for the number of students

for i in range(students):
    mark = input("Enter Letter Grade: ")
    marks.append(mark)

# Replace grade values with numeric values in array
for (k, index) in enumerate(marks):

    if index == "A":
        marks[k] = 80

    elif index == "B":
        marks[k] = 70

    elif index == "C":
        marks[k] = 60

    elif index == "D":
        marks[k] = 50

    elif index == "F":
        marks[k] = 40

# Count Passing Students
a_count = marks.count(80)
passing = passing + a_count

b_count = marks.count(70)
passing = passing + b_count

c_count = marks.count(60)
passing = passing + c_count

d_count = marks.count(50)
passing = passing + d_count

# Count Failing Students
f_count = marks.count(40)
failing = failing + f_count

# Calculate Average
average = sum(marks) / students

# Print results to the teacher
print("Class AVERAGE: " + str(round(average)))
print("Failing Students: " + str(failing))
print("Passing Students: " + str(passing))
