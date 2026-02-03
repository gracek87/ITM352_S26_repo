# Parse though the portions of an email address
# Name: Grace Kulhanek
# Date: 02/03/2026

# Method 1: Using split() to separate username and domain
email = input("Enter your email address: ")

parts = email.split("@")
username = parts[0]
domain = parts[1]

print("Username:", username)
print("Domain:", domain)   

# Method 2: Using index() and slicing to separate username and domain
atSymbolIndex = email.index("@")
usernameManuel = email[:atSymbolIndex]
domainManuel = email[atSymbolIndex + 1:]

print("Username (Manual):", usernameManuel)
print("Domain (Manual):", domainManuel)


