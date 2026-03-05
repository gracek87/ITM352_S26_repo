searchMe = [2, 5, 7, 11, 15, 22, 27, 30, 34, 41, 55, 57, 58, 60, 77]

userNum = int(input("Enter a number: "))
found = False

for num in searchMe:
    if userNum == num:
        found = True

if found:
    print("Number exists in the array.")
else:
    print("Number does not exist in the array.")