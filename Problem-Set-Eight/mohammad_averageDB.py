# Name: Nayalash Mohammad
# Date: November 02 2019
# File Name: averageDB.py
# Description: A program that takes four grade averages, and finds the total average.

def main():
    # Ask user for their grades in list format
    grades = input("Please specify your 4 course marks: ").split(",")

    # Splice List
    grades = grades[:4]

    # Start total off with nothing
    total = 0

    # Iterate over list provided, and add to the total
    for grade in grades:
        try:
            number = int(grade)
        except ValueError:
            print("Invalid Data Type... Try Again...")
            exit()
        total += number

    # Print Results
    print(f"""Your average is {total / 4}%""")

# Menu Method
def menu():
    
    print("To Run Program: type run, To Quit: type quit, For Help: type help")
    # Ask user for what they would like to do
    option = input()

    if (option == "run"):
        main() # Run App
        menu()
    elif (option == "quit"):
        exit()
    elif (option == "help"):
        print('To run program, type `run` below, or `quit` to quit the program. Refer to docs for more info.')
        print('Enter your four grades in (G1,G2,G3,G4) format.\nFor Example: 90,99,100,87')
        menu()
    else:
        print("Invalid Input")
        menu()

# Init Program
print("Welcome To Average Database")
menu()
