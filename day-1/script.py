with open('input.txt') as file:
    lines = file.readlines()
    file.close()

previous = "0"
counter = 0
for line in lines:
        if line > previous:
            counter = counter + 1
        previous = line
print("More depth: " + str(counter))