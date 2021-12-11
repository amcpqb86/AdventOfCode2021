file = open("input.txt", "r")
horizontal = 0
depth = 0

for lines in file:
    elements = lines.split(' ')
    if elements[0] == "forward":
        horizontal += int(elements[1])
    elif elements[0] == "down":
        depth += int(elements[1])
    elif elements[0] == "up":
        depth -= int(elements[1])

print(depth*horizontal)