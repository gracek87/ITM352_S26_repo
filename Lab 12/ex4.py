# Get public license data from the City of Chicagoʻs data portal

import pandas as pd 
from sodapy import Socrata

# Create a Sodapy client to access the City of Chicago's data portal
client = Socrata("data.cityofchicago.org", None)

# Specifiy the JSON file for the licsense data 

jsonFile = "rr23-ymwb"

results = client.get(jsonFile, limit=500)  

# Convert the results to a DataFrame for easier analysis 
df = pd.DataFrame.from_records(results)

print (df.head())

vehiclesAndFuelSources = df [["public_vehicle_number", "vehicle_fuel_source"]]
print("Public Vehicle Number and Fuel Source:")
print(vehiclesAndFuelSources.head())

vehiclesByFuelSource = df.groupby("vehicle_fuel_source").count()
print("Number of Vehicles by Fuel Source:")
print(vehiclesByFuelSource)

