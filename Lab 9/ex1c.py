# Open the file names.txt and read its contents and print the number of names

fileObject = open("names.txt")
contents = fileObject.read()
contentsList = contents.split("\n")
print(contentsList)
print("Number of names: " + str(len(contentsList)))
fileObject.close()