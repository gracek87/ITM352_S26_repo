# Use the input() function to get a name from the user and put it into title case.
# Name: Grace Kulhanek
# Date: 02/03/2026

rawName = input("Enter your full name: ")

titleName = rawName.strip().title()

#strippedName = rawName.strip()
#titleName = strippedName.title()
# ^ equivalent to line 5

print("Formatted Name:", titleName)
