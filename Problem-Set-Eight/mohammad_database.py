# Name: Nayalash Mohammad
# Date: November 05 2019
# File Name: database.py
# Description: A program that takes five names, and lets you try out DB operations.

def main():
    # Commands
    # display : will display all of them
    # displayspec [index] : will display a name at a certain index
    # edit [index] [newName] : edits index
    # and delete [index] : deletes at index
    running = True
    hasInitNames = False
    nameList = []

    def display(nameList):
        print("Your names: ")
        for name in nameList:
            print(name.strip())

    while running:
        if not hasInitNames:
            names = input("Please provide 5 names: ")
            nameList = names.split(",")
            nameList = nameList[:5]
            display(nameList)
            hasInitNames = True
        else:
            command = input()
            if command.lower() == "display":
                display(nameList)
            elif command.lower().startswith("edit"):
                arguments = command.split(" ")
                if len(arguments) > 2:
                    index = int(arguments[1])
                    if(index < len(nameList) and index > -1):
                        newName = arguments[2]
                        oldName = nameList[index]
                        nameList[index] = newName
                        print(f"""Replaced name {oldName} with {newName}""")
            elif command.lower().startswith("displayspec"):
                arguments = command.split(" ")
                if len(arguments) > 1:
                    index = int(arguments[1])
                    if(index < len(nameList) and index > -1):
                        print(f"""Name: {nameList[index]}""")
            elif command.lower().startswith("delete"):
                arguments = command.split(" ")
                if len(arguments) > 1:
                    index = int(arguments[1])
                    if(index < len(nameList) and index > -1):
                        deletedName = nameList[index]
                        del nameList[index]
                        print(f"""Deleted name '{deletedName}""")

            else:
                print("Command Not Valid Try Again....")
                exit()

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
        print('Enter your 5 names in this format : (name1,name2,name3,name4)')
        print('To Display Names, type command `display`')
        print('To display a specific name, type command `displayspec [index]`. For example: displayspec 1')
        print("Reminder Arrays Start at Zero!!!")
        print('To edit name, type command `edit [index] [newName]`. For example edit 1 sam')
        print('To delete name, type command `delete [index]`. For example delete 1')
        menu()
    else:
        print("Invalid Input")
        menu()

# Init Program
print("Welcome To Name Database")
menu()
