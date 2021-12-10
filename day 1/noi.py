def numberOfIncreases(file):
    file = open(file, "r")
    increases = 0
    ancientValue = 0

    for line in file:
        line = int(line)
        if line > ancientValue :
            increases += 1
        ancientValue = line
    
    file.close()
    return increases-1