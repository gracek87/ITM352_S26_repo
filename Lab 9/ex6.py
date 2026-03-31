import csv

filename = "..//taxi_1000.csv"

with open(filename) as csvfile:
    csvReader = csv.reader(csvfile)

    totalFare = 0.0
    maxDistance = 0.0
    numRows = 0

    for line in csvReader:
        if numRows == 0:   # header row
            fareIndex = line.index("Fare")
            distanceIndex = line.index("Trip Miles")
            numRows += 1
            continue

        tripFare = float(line[fareIndex])
        tripDistance = float(line[distanceIndex])

        # Only include fares greater than $10
        if tripFare > 10:
            totalFare += tripFare
            if tripDistance > maxDistance:
                maxDistance = tripDistance

        numRows += 1

    if numRows > 1:
        averageFare = totalFare / (numRows - 1)

    print(f"Total fare (>$10): ${totalFare:.2f}")
    print(f"Average fare (>$10): ${averageFare:.2f}")
    print(f"Max trip distance (>$10 fares): {maxDistance}")