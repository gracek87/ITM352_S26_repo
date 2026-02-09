tripDurations = [1.1, 0.8, 2.5, 2.6]
tripFares = (6.25, 5.25, 10.50, 8.05)

# Create a list of dictionaries where each dictionaries represents a trip
tripsList =[
    {"duration": 1.1, "fare": 6.25},
    {"duration": 0.8, "fare": 5.25},
    {"duration": 2.5, "fare": 10.50},
    {"duration": 2.6, "fare": 8.05}
]

print("List of trip dictionaries:")
print(tripsList)

# trips = dict (zip(tripDurations, tripFares))
# print("\ntrips dictionary:")
# print(trips)

tripNum = input("What trip do you want? [1-4]: ")
tripIndex = int(tripNum) - 1

print(f"Duration: {tripsList[tripIndex]['duration']} miles")
print(f"Fare: ${tripsList[tripIndex]['fare']:.2f}")

# print(f"Duration: {list(trips.keys())[tripIndex]} miles")
# print(f"Fare: ${list(trips.values())[tripIndex]:.2f}")
