# Get the Hawaii mortgage rates page and extract each bank with its rates
# Find the rate table and extract each row.
# Output the name of each bank and its current rates per row.


import requests
from bs4 import BeautifulSoup

mortgageRatesPage = requests.get("https://www.hicentral.com/hawaii-mortgage-rates.php")
htmlToParse = BeautifulSoup(mortgageRatesPage.text, "html.parser")
print("Hawaii Mortgage Rates:\n")


pageText = htmlToParse.get_text("\n", strip=True).split("\n")


mortgageRows = []
currentBank = ""

for i, line in enumerate(pageText):
    cleanLine = line.strip()

    if cleanLine in [
        "American Savings Bank",
        "Bank of Hawaii",
        "Central Pacific Bank",
        "Finance Factors",
        "First Hawaiian Bank",
        "Hawaii State Federal Credit Union",
        "Imperial Mortgage LLC",
        "Kama'aina Mortgage Group"
    ]:
        currentBank = cleanLine

    # Identify rate rows
    elif ("15-YR Fixed" in cleanLine or "30-YR Fixed" in cleanLine or "5-YR ARM" in cleanLine) and currentBank != "":
        mortgageRows.append([currentBank, cleanLine])


# Print each bank and its rates per row
for row in mortgageRows:
    print(row[0], "-", row[1])