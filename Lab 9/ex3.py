# Read the 1,000 lines of taxi data from the taxi_1000.csv file
# Calculate the total of all fares, average fare, and the max
# trip distance.

import csv

filename = "..//taxi_1000.csv"
with open(filename) as csvfile:
    csvReader = csv.reader(csvfile)

    totalFare = 0.0
    maxDistance = 0.0
    averageFare = 0.0
    numRows = 0

    for line in csvReader:
        if (numRows == 0):  # Skip the header row and find the index of the fare and distance columns
            fareIndex = line.index("Fare")
            distanceIndex = line.index("Trip Miles")
            numRows += 1
            continue
        if (numRows > 0):  # Skip the header row
            tripFare = float(line[fareIndex])  # Fare is in the specified column
            tripDistance = float(line[distanceIndex])  # Trip distance is in the specified column
            totalFare += tripFare
            if tripDistance > maxDistance:
                maxDistance = tripDistance
        numRows += 1

    if numRows > 0:  # Ensure there are data rows to calculate average
        averageFare = totalFare / (numRows - 1)  # Subtract 1 to exclude the header row

    print(f"We read {numRows - 1} rows of data.")
    print(f"Total fare: ${totalFare:.2f}")
    print(f"Average fare: ${averageFare:.2f}")
    print(f"Max trip distance: {maxDistance}")