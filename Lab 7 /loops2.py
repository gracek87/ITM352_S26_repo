prices = [100, 50, 20, 356]

total = 0
itemCount = 0

for price in prices:
    itemCount += 1
    if itemCount > 2 :
        discountedPrice = price * 0.9  # Apply a 10% discount
    else:
        discountedPrice = price 
    total += discountedPrice

roundedTotal = round(total, 2)  # Round the total to 2 decimal places
print(f"Total price: ${roundedTotal:.2f}")


