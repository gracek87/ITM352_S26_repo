# Get a JSON file from the City of Chicago's data portal and analyze driver types

import pandas as pd
import requests 

# Create a REST query to get the JSON file for driver types

searchResults = requests.get("https://data.cityofchicago.org/resource/97wa-y6ff.json?$select=driver_type,count(license)&$group=driver_type")

resultsJSON = searchResults.json()
print ("Driver Types and License Counts:")
print(resultsJSON)

# Convert the results to a DataFrame for easier analysis
df = pd.DataFrame(resultsJSON)
results_df.columns = ["driverType", "LicsenseCount"]
results_df = results_df.set_index("driverType")

print("\nLicense Counts by Driver Type:")
print(results_df)