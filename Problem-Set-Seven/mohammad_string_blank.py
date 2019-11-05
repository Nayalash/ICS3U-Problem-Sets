# Author: Nayalash Mohammad
# Date: November 01 2019
# File Name: string_blank.py
# Description: A program that replaces multiple spaces with one

# Main Code
def main():
	# Ask for string
	string = input("Enter a string with multiple blank spaces...\n")

	# Regex the string, and join it
	newString = ' '.join(string.split())

	print("********************************")
	# Display Results
	print("Your Formatted String is: ")
	print(newString)
	# Re-Run
	menu()


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
        print('Type your spaced out text, and the program will format it for you.')
        menu()
    else:
        print("Invalid Input")
        menu()

# Init Program
print("Welcome To String Formatter")
menu()


