def getCharacterFrequencies(inputString):
    frequencies = {}

    for char in inputString:
        char = char.lower()  # Convert to lowercase for case-insensitive counting
        if char in frequencies:
            frequencies[char] += 1
            print ("Get a new character: " + char)
        else:
            frequencies[char] = 1
    return frequencies

mydict = getCharacterFrequencies("Snow White and the Seven Dwarfs")
print(mydict)
sortedByKeys = dict(sorted(mydict.items()))
print(sortedByKeys)

