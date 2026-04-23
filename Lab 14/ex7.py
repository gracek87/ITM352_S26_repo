# Create a 3D scatterplot of fares, trip miles, and dropoff area
import matplotlib.pyplot as plt
import pandas as pd
from mpl_toolkits.mplot3d import Axes3D

trips_df = pd.read_json("Trips from area 8.json")

fare_series = trips_df["fare"]
trip_series = trips_df["trip_miles"]
dropoff_series = trips_df["dropoff_community_area"]

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

ax.scatter(trip_series, fare_series, dropoff_series)
ax.set_title("3D Plot of Fares, Trip Miles, and Dropoff Area")
ax.set_xlabel("Trip Miles")
ax.set_ylabel("Fares in $")
ax.set_zlabel("Dropoff Area") #3D

plt.show()