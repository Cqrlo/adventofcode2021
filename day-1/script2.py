# data in var zetten
with open('input.txt') as file:
    lines = file.readlines()
    file.close()

# vars declaren
totalprevious = 1
current1 = 0
current2 = 0
current3 = 0
totalcurrent = 1
counter = 0
x = 0
listlength = len(lines)

# main loop
for line in lines:
    # current maken
    current1 = int(lines[x])
    current2 = int(lines[x + 1])
    current3 = int(lines[x + 2])
    totalcurrent = current1 + current2 + current3

    # checken
    if totalcurrent > totalprevious:
        counter += 1

    # klaar maken voor volgende iteration
    totalprevious = totalcurrent
    x += 1

    # kijken of loop moet stoppen
    if x + 3 >= listlength:
        break

# print
print(counter)