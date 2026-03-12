# Open the file names.txt and read its contents and print the number of names

with open("names.txt") as fileObject:
    contentsList = fileObject.readlines()
    print(contentsList)


with open("names.txt", "a") as fileObject:
    print("appending new name to the file...")
    fileObject.write("Kulhanek, Grace\n")
    contentsList.append("Kulhanek, Grace\n")
    print("Number of names: " + str(len(contentsList)))
