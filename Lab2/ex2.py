# Ask the user to enter their birth year and calculate their age based on the current year (2026). Print the user's age.
# Name: Grace Kulhanek
# Date: 01/20/2026

birthYear = input("Please enter your birth year: ")
birthYearInteger = int(birthYear)
currentYear = 2026
age = currentYear - birthYearInteger
print("You entered:", birthYear)
print(f"You are {age} years old.")