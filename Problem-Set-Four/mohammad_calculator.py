# Name: Nayalash Mohammad
# Date: October 12 2019
# File Name: leap_year.py
# Description: A program that asks a user for a year,
# that tells if a year is a leap year or not.

def calculate():
    operation = input("What Mathematical Operation Do You Want To Perform?"
                      "\naddition = a, subtraction = s, multiplication = m, "
                      "division = d, modulo = mod, exponent = e \n ")

    numOne = int(input("Enter Number One: "))
    numTwo = int(input("Enter Number Two: "))


    if (operation == "a"):
        answer = numOne + numTwo
        print("The answer is : " + str(answer))

    elif (operation == "s"):
        answer = numOne - numTwo
        print("The answer is : " + str(answer))

    elif (operation == "m"):
        answer = numOne * numTwo
        print("The answer is : " + str(answer))

    elif (operation == "d"):
        answer = numOne / numTwo
        print("The answer is : " + str(answer))

    elif (operation == "mod"):
        answer = numOne % numTwo
        print("The answer is : " + str(answer))
    elif (operation == "e"):
        answer = numOne ** numTwo
        print("The answer is : " + str(answer))

def menu():
    option = input()

    if (option == "run"):
        calculate()
        menu()
    elif (option == "quit"):
        exit()
    elif (option == "help"):
        print('HI')
        menu()
    else:
        print("Invalid Input")
        menu()



print("Welcome To The Calculator App \n To Run Program: type run, To Quit: type quit, For Help: type help")
menu()