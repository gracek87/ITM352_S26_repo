# Read in a CSV file and create a dataframe
# Print some useful info

import pandas as pd
import numpy as np

filename =  "https://drive.google.com/uc?id=1ujY0WCcePdotG2xdbLyeECFW9lCJ4t-K"

pd.set_option('display.max_columns', None)  # Show all columns

df = pd.read_csv(filename, engine="pyarrow")
df["order_date"] = pd.to_datetime(df["order_date"], errors="coerce") # Convert order_date to datetime, coercing errors to NaT

# Print some useful info
print(df.info())
print(df.describe())
print(df.head(5))