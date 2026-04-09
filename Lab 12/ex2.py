import ssl 
import pandas as pd
import urllib.request
import lxml


url = "https://home.treasury.gov/resource-center/data-chart-center/interest-rates/TextView?type=daily_treasury_yield_curve&field_tdr_date_value_month=202603"

# Open the URL and use read_HTML to read the data into a DataFrame
ssl._create_default_https_context = ssl._create_unverified_context

print("Opening URL: " + url)
webPage = urllib.request.urlopen(url)
dataFrame = pd.read_html(webPage)

#print(dataFrame[0].info)
#print(dataFrame[0])

# Extract the 1 month interest rate data 
oneMonthData = dataFrame[0].loc[0, "1 Mo"]

# Iterate through the data using iterrows() to find the 1 month rate for a specific date
for index, row in dataFrame[0].iterrows():
    if row["Date"] == "03/01/2026":
        oneMonthRate = row["1 Mo"]
        print(f"The 1 month interest rate on 03/01/2026 was: {oneMonthRate}")
        break


