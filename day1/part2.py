# Day 1 - Part 2

from noi import numberOfIncreases as noi

file = open("input.txt", "r")
outputFile = open("out.txt", "w")

lines = file.readlines()

for position in range(len(lines) - 2):
    sum = int(lines[position]) + int(lines[position+1]) + int(lines[position+2])
    outputTexte = str(sum) + "\n"
    outputFile.write(outputTexte)

outputFile.close()

print(noi("out.txt"))
