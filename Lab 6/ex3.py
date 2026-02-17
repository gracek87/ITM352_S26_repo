def determineProgress1(hits, spins):
    if spins == 0:
        return "Get going!"
    
    hits_spins_ratio = hits / spins

    if hits_spins_ratio > 0:
        progress = "On your way!"
        if hits_spins_ratio >= 0.25:
            progress = "Almost there!"
            if hits_spins_ratio >= 0.5:
                if hits < spins:
                    progress = "You win!"
    else:
        progress = "Get going!"

    return progress


def testDetermineProgress(ProgressFunction):
    """Test function for testDetermineProgress using assert statements.
    
    Test cases cover all four possible return values:
    1. "Get going!" when spins =0 (edge case)
    2. "Get going!" when hits/spins <= 0 (ratio of 0)
    3. "On your way!" when 0 < hits/spins < 0.25
    4. "Almost there!" when 0.25 <= hits/spins < 0.5
    5. "You win!" when hits/spins >= 0.5 and hits < spins
    """
    # Test case 1: spins = 0 (edge case)
    assert ProgressFunction(10, 0) == "Get going!", "Test case 1 failed: hits/spins = 0"

    # Test case 2: hits/spins <= 0 (ratio of 0)
    assert ProgressFunction(0, 10) == "Get going!", "Test case 2 failed: hits/spins = 0"
    
    # Test case 3: 0 < hits/spins < 0.25
    assert ProgressFunction(1, 10) == "On your way!", "Test case 3 failed: 0 < hits/spins < 0.25"
    
    # Test case 4: 0.25 <= hits/spins < 0.5
    assert ProgressFunction(1, 4) == "Almost there!", "Test case 4 failed: 0.25 <= hits/spins < 0.5"
    
    # Test case 5: hits/spins >= 0.5 and hits < spins
    assert ProgressFunction(6, 10) == "You win!", "Test case 5 failed: hits/spins >= 0.5 and hits < spins"

    # Test case 6: hits/spins >= 0.5 but hits >= spins (should not return "You win!")
    assert ProgressFunction(11, 10) == "Almost there!", "Test case 6 failed: hits/spins >= 0.5 but hits >= spins"

def determineProgress2(hits, spins):
    if spins == 0:
        return "Get going!"

    hits_spins_ratio = hits / spins

    if hits_spins_ratio <= 0:
        return "Get going!"

    if hits_spins_ratio > 0 and hits_spins_ratio < 0.25:
        return "On your way!"

    if hits_spins_ratio >= 0.25 and hits_spins_ratio < 0.5:
        return "Almost there!"

    if hits_spins_ratio >= 0.5 and hits < spins:
        return "You win!"

    if hits_spins_ratio >= 0.5 and hits >= spins:
        return "Almost there!"

def determineProgress3(hits, spins):
    if spins == 0:
        return "Get going!"

    ratio = hits / spins

    if ratio <= 0:
        return "Get going!"
    elif ratio < 0.25:
        return "On your way!"
    elif ratio < 0.5:
        return "Almost there!"
    elif hits < spins:
        return "You win!"
    else:
        return "Almost there!"

# Give an example variation of determine_progress1 that can be used to implement the logic for the function that does not use if-statements and explain its advantages and disadvantages.

def determineProgress4(hits, spins):
    ratio = hits / spins if spins != 0 else 0

    conditions = {
        "You win!": (spins != 0 and ratio >= 0.5 and hits < spins),
        "Almost there!": (spins != 0 and ratio >= 0.25),
        "On your way!": (spins != 0 and ratio > 0),
        "Get going!": True
    }

    for message, condition in conditions.items():
        if condition:
            return message

print("All tests passed!")
testDetermineProgress(determineProgress1)

print("All tests passed!")
testDetermineProgress(determineProgress2)

print("All tests passed!")
testDetermineProgress(determineProgress3)

print("All tests passed!")
testDetermineProgress(determineProgress4)





 
