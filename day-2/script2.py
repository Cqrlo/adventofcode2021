with open('input.txt') as file:
    lines = file.readlines()
    file.close()

horizontal = 0
depth = 0
aim = 0
currentLineSplit = [" ", " "]

for line in lines:
    currentLineSplit = line.split()
    if (currentLineSplit[0] == "forward"):
        horizontal += int(currentLineSplit[1])
        depth      += int(currentLineSplit[1]) * aim
    elif (currentLineSplit[0] == "up"):
        aim        -= int(currentLineSplit[1])
    elif (currentLineSplit[0] == "down"):
        aim        += int(currentLineSplit[1])

print(horizontal * depth)