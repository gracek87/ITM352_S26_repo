# Ask the user to enter their weight in pounds
# Convert the weight to kilograms (1 pound = 0.453592 kg)
# Name: Grace Kulhanek
# Date: 01/22/2026

kgToPounds = 0.453592

weightInPounds = input("Please enter your weight in pounds: ")
weightPoundsFloat = float(weightInPounds)
weightKilograms = weightPoundsFloat * kgToPounds
weightKilogramsRounded = round(weightKilograms)

print("You entered:", weightPoundsFloat, "lbs")
print(f"Your weight in kilograms is: {weightKilogramsRounded} kg")