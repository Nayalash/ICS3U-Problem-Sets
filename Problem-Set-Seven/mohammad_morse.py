# Author: Nayalash Mohammad
# Date: November 02 2019
# File Name: morse.py
# Description: A program that converts english to morse code

# Initialize All Morse Code Characters to English Characters
Dictionary = {
'A': '.-',
'B': '-...',
'C': '-.-.', 
'D': '-..',    
'E': '.',      
'F': '..-.',
'G': '--.',    
'H': '....',   
'I': '..',
'J': '.---',   
'K': '-.-',    
'L': '.-..',
'M': '--',     
'N': '-.',     
'O': '---',
'P': '.--.',   
'Q': '--.-',   
'R': '.-.',
'S': '...',    
'T': '-',      
'U': '..-',
'V': '...-',   
'W': '.--',    
'X': '-..-',
'Y': '-.--',   
'Z': '--..',
'0': '-----',  
'1': '.----',  
'2': '..---',
'3': '...--',  
'4': '....-',  
'5': '.....',
'6': '-....',  
'7': '--...',  
'8': '---..',
'9': '----.' 
}

# Main Code
def main():
	
	string = input("String: ")
	
	for i in string:
        # Convert to upper case, as initialized in dictionary above
		print(Dictionary[i.upper()])


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
        print('Type your text, and the program will convert it to Morse Code.')
        menu()
    else:
        print("Invalid Input")
        menu()

# Init Program
print("Welcome To Morse Converter")
menu()



