import random

# Generate data
data = []
index = 0
for totalIndex, i in enumerate(range(random.randint(360, 1080))):
    index += 1
    if(index < 360):
        data.append(random.randint(1, 2))
    else:
        data.append(random.randint(0, 2))
        if(data[totalIndex] == 0):
            index = 0

# Parse data
parsedData = [[]]
index = 0
for signal in data:
    if not signal == 0:
        parsedData[index].append(signal)
    else:
        index += 1
        parsedData.append([])

print()

for num, survey in enumerate(parsedData):
    print(f"""Stats for survey #{num + 1}""")
    print(f"""The survey is {len(survey)} seconds long""")
    print(f"""There were {survey.count(2)} vehicles""")

    longestTime = 0
    currentTime = 0
    for i in survey:
        if i == 1:
            currentTime += 1
        else:
            if currentTime > longestTime:
                longestTime = currentTime
            currentTime = 0
    print(f"Longest time without vehicles was {longestTime} seconds")
    print(f"Averaged {round((survey.count(2) / len(survey)) * 60)} vehicles per minute.")

    print()