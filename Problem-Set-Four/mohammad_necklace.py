# Name: Nayalash Mohammad
# Date: October 12 2019
# File Name: necklace.py
# Description: A program that follows the necklace algorithm

# Ask user for their first and second number
numberOne = int(input("Enter first number: "))
numberTwo = int(input("Enter second number: "))

# Assign Place Holders
initNumberOne = numberOne
initNumberTwo = numberTwo

complete = False

counter = 0

# Add a continuous loop
while (not complete):
    counter += 1

    iteration = numberOne + numberTwo

    # Has to be single digit number
    if (iteration > 10):
        iteration -= 10

    print(iteration)

    numberOne = numberTwo
    numberTwo = iteration

    if(numberOne == initNumberOne and numberTwo == initNumberTwo):
        print("^ Steps: " + str(counter + 2)) # Print the steps taken
        # Exit out of loop
        complete = True

print("NL has been printed")
