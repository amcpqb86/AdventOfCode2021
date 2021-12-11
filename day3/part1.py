file = open("input.txt", "r")
lines = file.readlines()

gamma = ""
epsilon = ""

for column in range(12):
    count0 = 0
    count1 = 0
    for line in lines:
        if line[column] == "0":
            count0 += 1
        else :
            count1 += 1
    if count0 > count1 :
        gamma += "0"
        epsilon += "1"
    else :
        gamma += "1"
        epsilon += "0"


print(int(gamma, 2) * int(epsilon, 2))