
# Ask user for their grades in list format
grades = input("Please specify your 4 course marks: ").split(",")

# Splice Array
grades = grades[:4]

# Start total off with nothing
total = 0

# Iterate over list provided, and add to the total
for grade in grades:
    number = int(grade)
    total += number

print(f"""Your average is {total / 4}%""")