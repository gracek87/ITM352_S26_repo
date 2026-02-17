age = int(input("Enter your age: "))
weekday = input("Enter the weekday: ")
matinee = input("Is it a matinee? (yes/no): ").lower() == "yes"

price = 14

if matinee and age >= 65:
    price = 5
elif matinee:
    price = 8
elif age >= 65:
    price = 8
elif weekday == "Tuesday":
    price = 10

print("Age:", age)
print("Weekday:", weekday)
print("Matinee:", matinee)
print("Price: $", price)