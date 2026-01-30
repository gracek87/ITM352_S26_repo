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

def exponent ( base, exp, precision=2 ):
    """Calculate the base raised to the power."""
    result = base ** exp
    roundedResult = round(result, precision)
    return roundedResult

def max(num1, num2):
    """Return the maximum of two numbers."""
    return num1 if num1 > num2 else num2

def min(num1, num2):
    """Return the minimum of two numbers."""
    return num1 if num1 < num2 else num2

def apply_function(x, y, func):
    """Apply a given function to x and y and return a formatted string."""
    result = func(x, y)
    return f"The function {func.__name__} {x},{y} = {result}"