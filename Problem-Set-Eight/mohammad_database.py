

# Commands
# display: will display all of them
# displayspec [index] :will display a name at a certain index
# edit [index] [newName]: edits index
# and delete [index] deletes at index

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