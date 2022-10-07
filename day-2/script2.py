with open('input.txt') as file:
    lines = file.readlines()
    file.close()

previous = "0"
current = 0
counter = 0
x = 0
#for lines in range(x, 3):
for line in lines:
        current += line
        if current > previous:
            counter += 1
        previous = line
        x += 1
print("More depth: " + str(counter))