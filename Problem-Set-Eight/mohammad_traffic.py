# Name: Nayalash Mohammad
# Date: November 07 2019
# File Name: traffic.py
# Description: A program that follows the traffic algorithm, provided by the problem set.

# Import Random Lib To use Randint Function
import random

# Main Code
def main():
    # Init Data Array and index counter
    data = []
    index = 0

    # Generate data
    for totalIndex, i in enumerate(range(random.randint(360, 1080))):
        # Add one each time to index
        index += 1

        # Randomize the signals
        if(index < 360):
            # Signal Config
            data.append(random.randint(1, 2))
        else:
            # Signal Config
            data.append(random.randint(0, 2))
            # Start Loop Over
            if(data[totalIndex] == 0):
                index = 0

    # Parse data
    parsedData = [[]]
    index = 0

    # Add The Signal into Array
    for signal in data:
        # Store Based on Signal
        if not signal == 0:
            parsedData[index].append(signal)
        else:
            index += 1
            parsedData.append([])

    # Line Breaker
    print()

    # Loop through Survey
    for num, survey in enumerate(parsedData):
        # Print the results for each survey
        print(f"""Stats for survey #{num + 1}""")
        print(f"""The survey is {len(survey)} seconds long""")
        print(f"""There were {survey.count(2)} vehicles""")

        # Account for following data
        longestTime = 0
        currentTime = 0

        # Calculate timings
        for i in survey:
            # Iterates current time
            if i == 1:
                currentTime += 1
            else:
                # Evaluate Total Time
                if currentTime > longestTime:
                    longestTime = currentTime
                currentTime = 0

        # Print timings
        print(f"Longest time without vehicles was {longestTime} seconds")
        print(f"Averaged {round((survey.count(2) / len(survey)) * 60)} vehicles per minute.")

        # Line Breaker
        print()