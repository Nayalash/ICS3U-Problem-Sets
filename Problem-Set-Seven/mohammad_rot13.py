# Author: Nayalash Mohammad
# Date: November 04 2019
# File Name: date.py
# Description: A program that follows the ROT13 algorithm.


# Main Code
def main():

    # Ask for user text
    text = input("Enter a text: ")

    # Define array for alphabet
    alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

    # Encrypt Function
    def encrypt(text):
        encryptedText = ""

        for letter in text:
            oldIndex = alphabet.index(letter)
            # Move 13 up
            newIndex = oldIndex + 13
            # Check for string end
            if newIndex > 25:
                newIndex -= 26
            encryptedText += alphabet[newIndex]
        return encryptedText
    
    # Decrypt Function
    def decrypt(text):
        decryptedText = ""

        for letter in text:
            oldIndex = alphabet.index(letter)
            # Move 13 down
            newIndex = oldIndex - 13
            # Check for string end
            if newIndex > 25:
                newIndex -= 26
            decryptedText += alphabet[newIndex]
        return decryptedText

    # Match text with array
    encrypted = encrypt(text.lower())
    # Print Results
    print(encrypted)
    print(decrypt(encrypted))


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
        print('Type in text and the program will decrypt and encrypt for you')
        menu()
    else:
        print("Invalid Input")
        menu()

# Init Program
print("Welcome To ROT13 Cipher")
menu()
