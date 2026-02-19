recentPurchases = [36.13, 23.87, 183.35, 22.93, 11.62]

budget = 200 
totalSpent = 0

for purchase in recentPurchases:
    totalSpent += purchase
    
    if totalSpent > budget:
        print("This purchase is over your budget.", purchase)
    else:
        print("This purchase is within your budget.", purchase)


# def checkBudget (purchase, limit):