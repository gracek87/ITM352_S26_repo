celebs = ("Taylor Swift", "Lionel Messi", "The Weeknd", "Keanu Reeves", "Angelina Jolie")
ages = (36, 38, 36, 61, 50)

celebsList = []
for celeb in celebs:
    celebsList.append(celeb)

agesList = [age for age in ages]

celebsDict = {"celebrities": celebsList, "ages": agesList}

print(celebsDict)

celebsDict = {
    "celebrities": list(celebs),
    "ages": list(ages)
}

print(celebsDict)

