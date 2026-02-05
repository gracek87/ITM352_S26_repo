countryCapitals = {
    "Germany": "Berlin",
    "Canada": "Ottawa",
    "England": "London",
    "Italy": "Rome",
}   

print(countryCapitals)

print(countryCapitals["Canada"])
print(countryCapitals["England"])

countryCapitals["Spain"] = "Madrid"
print(countryCapitals)  

print("Germany" in countryCapitals)
print("Switzerland" not in countryCapitals)
print("Korea" in countryCapitals)

