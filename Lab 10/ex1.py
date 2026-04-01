# Creates a list of tuples that are percentailes of the household incpme
import numpy as np

percentile_income = [
    (10, 14629),
    (20, 25600),
    (30, 37002),
    (40, 50000),
    (50, 63179),
    (60, 79542),
    (70, 100162),
    (80, 130000),
    (90, 184292)
]

hhIncomeArray = np.array(percentile_income)

# Report the dimensions of the array, and the number of elements in the array
print("Dimensions of the Array: ", hhIncomeArray.ndim)
print("Dimension v2 ", hhIncomeArray.shape)
print("Number of elements in the Array: ", hhIncomeArray.size)

for i in range (len(hhIncomeArray)):
    print(i, hhIncomeArray[i][0], hhIncomeArray[i][1])