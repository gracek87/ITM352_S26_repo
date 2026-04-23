# Create a heatmap of pickup and dropoff community areas
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

trips_df = pd.read_csv("taxi trips Fri 7_7_2017.csv")

pickup_series = trips_df["pickup_community_area"]
dropoff_series = trips_df["dropoff_community_area"]

# Create a cross-tab for heatmap
heatmap_data = pd.crosstab(pickup_series, dropoff_series)

fig = plt.figure()

sns.heatmap(heatmap_data)
plt.title("Heatmap of Pickup vs Dropoff Community Areas")
plt.xlabel("Dropoff Area")
plt.ylabel("Pickup Area")

plt.show()