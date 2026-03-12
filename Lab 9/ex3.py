# Read the 1000 lines of taxi data from the taxi_1000.csv file
# Calculate the total of all fares, average fare, and the max fare 
# trip distance

import csv 

filename = "..//taxi_1000.csv"
with open(filename) as csvfile:
    csvreader = csv.reader(csvfile)

    totalFare = 0.0
    maxDistance = 0.0
    averageFare = 0.0
    numberRows = 0

    for line in csvreader:
        if (numberRows == 0):   # Skip header row
            fareIndex = line.index("Fare")
            distanceIndex = line.index("Trip Miles")
            numberRows += 1
            continue
        if numberRows > 0:  # Skip the header row
            tripFare = float(line[fareIndex])  # Fare is in the specified column index
            tripDistance = float(line[distanceIndex])  # Trip distance is in the specified column index
            totalFare += tripFare
            if tripDistance > maxDistance:
                maxDistance = tripDistance
        numberRows += 1

    if numberRows > 1: # Ensure there are data rows to calculate the average 
        averageFare = totalFare / (numberRows - 1)  # Subtract 1 to account for the header row

    print (f"We read")
    print (f"Total fare: {totalFare}")
    print (f"Average fare: {averageFare}")
    print (f"Max distance: {maxDistance}")  