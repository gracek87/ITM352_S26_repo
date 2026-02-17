# Write Python code that creates a list with a variety of different values. Include control logic (if, elif, else) that will print different messages whether the list contains fewer than 5 elements, between 5 and 10 (inclusive), and more than 10 elements. Test your code on lists with several different lengths.


myList = [7, "Grace", 3.14, True, "ITM352", 42]

# Control logic based on list length
if len(myList) < 5:
    print("This list has fewer than 5 elements.")
elif 5 <= len(myList) <= 10:
    print("This list has between 5 and 10 elements (inclusive).")
else:
    print("This list has more than 10 elements.")

testLists = [
    [1, 2],                                  # length 2
    [1, 2, 3, 4, 5],                          # length 5
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],          # length 10
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]       # length 11
]

for lst in testLists:
    if len(lst) < 5:
        print(lst, "-> fewer than 5 elements")
    elif 5 <= len(lst) <= 10:
        print(lst, "-> between 5 and 10 elements (inclusive)")
    else:
        print(lst, "-> more than 10 elements")

def describeListSize(lst):
    n = len(lst)
    if n < 5:
        return "fewer than 5 elements"
    elif n <= 10:  # same as 5 <= n <= 10 because we already know n >= 5 here
        return "between 5 and 10 elements (inclusive)"
    else:
        return "more than 10 elements"

for lst in testLists:
    print(f"Length: {len(lst)} -> {describeListSize(lst)}")
