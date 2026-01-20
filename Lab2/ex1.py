# Ask the user for a number between 1 and 100. Square the number and print the number and its square. 
# Name: Grace Kulhanek
# Date: 01/20/2026

print ("Welcome to the Program!")
valueUserEntered =input (" Please enter a number between 1 and 100: ")
print ("You entered: ", valueUserEntered)

valueAsInteger = int(valueUserEntered)
squaredValue = valueAsInteger ** 2
#print ("The square of", valueAsInteger, "is", squaredValue)
print(f"The square of {valueAsInteger} is {squaredValue}")