# Write Python code that initializes a tuple of strings representing different emotions (i.e., happy, sad, fear, surprise). Write code that uses a conditional expression (do not use an if-statement or ternary expression) to print “true” if the last element is “happy” and there are more than 3 elements, or “false” if it is not.
# Name: Grace Kulhanek
# Date: 02/10/2026

emotions = ("happy", "sad", "fear", "surprise")
result = [(emotions[-1] == "happy") and (len(emotions) > 3)]
result2 = [(emotions[-1] == "surprise") and (len(emotions) > 3)]
print(result)
print(result2)

# part B

if(result == [True]):
    print("true")
else:
    print("false")
