# This program demonstrates the concept of variable scope in Python.
# Name: Grace Kulhanek
# Date: 01/27/2026

def calculateDiscountedPrice(price):
    #global discount
    discount = 0.9
    price *= discount
    print(f"Inside function, discounted price: {price:.2f}")
    return price

discount = 0.6
price = 100
print(f"Original price before function call: {price:.2f}")
discountedPrice = calculateDiscountedPrice(price)

print(f"Original price after function call: {price:.2f}")
print(f"Discount=", discount)

