ata = ("hello", 10, "goodbye", "3", "goodnight", 5, 6.7, True)
user_input = input("Enter a value to add to the tuple: ")

# (a) Try to append (this will error) + (b) try/except report the error
try:
    data.append(user_input)  
except Exception as e:
    print("Attempted to append to the tuple, but an error occurred:")
    print("Error:", e)