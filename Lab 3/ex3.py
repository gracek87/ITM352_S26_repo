def sqrt(number):
    """Return the square root of a number."""
    if number < 0:
        return None
    return number ** 0.5

numberIn = float(input("Enter a positive number to find its square root: "))

result = sqrt(numberIn)
if result is None:
    print("Cannot compute the square root of a negative number.")
else:
    print(f"The square root of {numberIn} is {result:.2f}")
