with open('input.txt') as file:
    lines = file.readlines()
    file.close()

horizontal = 0
depth = 0
currentLineSplit = [" ", " "]

for line in lines:
    currentLineSplit = line.split()
    if (currentLineSplit[0] == "forward"):
        horizontal += int(currentLineSplit[1])
    if (currentLineSplit[0] == "up"):
        depth -= int(currentLineSplit[1])
    if (currentLineSplit[0] == "down"):
        depth += int(currentLineSplit[1])

print(horizontal * depth)