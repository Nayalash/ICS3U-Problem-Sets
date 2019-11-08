# Author: Nayalash Mohammad
# Date: November 03 2019
# File Name: date.py
# Description: A program that takes a date in MMDDYYYY and formats it.

# Main Code
def main():

    # Ask user for a date
    date = input("Please enter a date in MMDDYYYY format, e.g (04022003) : ")

    # Splice the data in the string
    month = int(date[0] + date[1])
    day = date[2] + date[3]
    year = date[4] + date[5] + date[6] + date[7]

    # Define Months Array
    months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']

    # Print Result to User
    print(f"""{day}, {months[month - 1]}, {year}""")

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
        print('Type your date in MMDDYYYY format (04022003), and the program will format it for you')
        menu()
    else:
        print("Invalid Input")
        menu()

# Init Program
print("Welcome To Date Formatter")
menu()
