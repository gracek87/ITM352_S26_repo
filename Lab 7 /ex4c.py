recentPurchases = [36.13, 23.87, 183.35, 22.93, 11.62]

budget = 200 
totalSpent = 0

def checkBudget(purchase, limit):
    return "This purchase is over budget!" if purchase > limit else "This purchase is within budget"

assert checkBudget(183.35, 50) == "This purchase is over budget!"
assert checkBudget(36.13, 50) == "This purchase is within budget"

print("All tests passed!")