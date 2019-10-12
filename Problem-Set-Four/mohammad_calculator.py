# Name: Nayalash Mohammad
# Date: October 12 2019
# File Name: calculator.py
# Description: A calculator program that can handle add/sub/div/mult/exp/mod
# operations, and continuously runs.

# Main Calculation Method
def calculate():

    # Ask user for inputs
    operation = input("What Mathematical Operation Do You Want To Perform?"
                      "\naddition = a, subtraction = s, multiplication = m, "
                      "division = d, modulo = mod, exponent = e \n ")

    numOne = int(input("Enter Number One: "))
    numTwo = int(input("Enter Number Two: "))

    # Use basic arithmetic algorithms

    if (operation == "a"):
        # Addition
        answer = numOne + numTwo
        print("The answer is : " + str(answer))
        print("To Run Again, type `run`")

    elif (operation == "s"):
        # Subtraction
        answer = numOne - numTwo
        print("The answer is : " + str(answer))
        print("To Run Again, type `run`")

    elif (operation == "m"):
        # Multiplication
        answer = numOne * numTwo
        print("The answer is : " + str(answer))
        print("To Run Again, type `run`")

    elif (operation == "d"):
        # Division
        answer = numOne / numTwo
        print("The answer is : " + str(answer))
        print("To Run Again, type `run`")

    elif (operation == "mod"):
        # Modulus
        answer = numOne % numTwo
        print("The answer is : " + str(answer))
        print("To Run Again, type `run`")

    elif (operation == "e"):
        # Exponent
        answer = numOne ** numTwo
        print("The answer is : " + str(answer))
        print("To Run Again, type `run`")


# Main Menu Method
def menu():

    # Ask user for what they would like to do
    option = input()

    if (option == "run"):
        calculate()
        menu()
    elif (option == "quit"):
        exit()
    elif (option == "help"):
        print('To run program, type `run` below, or `quit` to quit the program. Refer to docs for more info.')
        menu()
    else:
        print("Invalid Input")
        menu()

# Init Program
print("Welcome To The Calculator App \nTo Run Program: type run, To Quit: type quit, For Help: type help\n")
menu()