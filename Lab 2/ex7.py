# Ask the user to enter a temperature in Fahrenheit
# Convert the temperature to Celsius using the formula: (C = (F - 32) * 5/9)
# Name: Grace Kulhanek
# Date: 01/22/2026

farenheitInput = input("Please enter a temperature in Fahrenheit: ")
farenheitValue = float(farenheitInput)
celsiusValue = (farenheitValue - 32) * 5 / 9
celsiusValueRounded = round(celsiusValue, 1)

print("You entered:", farenheitValue, "°F")
print(f"The temperature in Celsius is: {celsiusValueRounded} °C")