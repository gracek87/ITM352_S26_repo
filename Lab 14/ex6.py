# Create a scatterplot of fares by trip miles (filtered)
import matplotlib.pyplot as plt
import pandas as pd

# Read in the data from the JSON file
trips_df = pd.read_json("Trips from area 8.json")

# Filter out 0 miles and trips less than 2 miles
filtered_df = trips_df[["trip_miles", "fare"]].query('trip_miles >= 2')

fare_series = filtered_df["fare"]
trip_series = filtered_df["trip_miles"]

fig = plt.figure()

plt.scatter(trip_series, fare_series)
plt.title("Fares by Trip Miles (>= 2 miles)")
plt.xlabel("Trip Miles")
plt.ylabel("Fares in $")
plt.savefig("FaresXmiles.png", dpi=300)
plt.show()