file = open("input.txt", "r")
increases = 0
ancientValue = 0

for line in file:
    line = int(line)
    if line > ancientValue :
        increases += 1
    ancientValue = line

print(increases-1) # On enlève 1 car le chiffre de la première ligne sera forcément supérieur à 0

file.close()