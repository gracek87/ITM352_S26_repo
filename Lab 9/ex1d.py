with open ("names.txt") as fileObject:
    while (line := fileObject.readline()):
        print(line.strip())
