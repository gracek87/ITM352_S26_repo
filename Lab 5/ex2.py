tripDurations = [1.1, 0.8, 2.5, 2.6]
tripFares = (6.25, 5.25, 10.50, 8.05)

taxiTrips = {
       "alles": tripDurations,
       "fares": tripFares
}

print(taxiTrips)

print(f"The third trip was {taxiTrips['alles'][2]} miles long.")
print(f"The fare for the third trip was ${taxiTrips['fares'][2]:.2f}.")