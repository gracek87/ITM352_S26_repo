# Handy library of mathematical functions
# Name: Grace Kulhanek
# Date: 01/27/2026

def midpoint(num1, num2):
    """Calculate the midpoint between two numbers."""
    mid = (num1 + num2) / 2
    return mid

def sqrt(number):
    """Calculate the square root of a number."""
    if number < 0:
        return None
    return number ** 0.5

def exponent ( base, exp, precision ):
    """Calculate the base raised to the power."""
    result = base ** exp
    roundedResult = round(result, precision)
    return roundedResult
