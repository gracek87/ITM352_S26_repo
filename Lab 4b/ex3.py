# Use the input() function to get a URL from the user
# Parse the string to get just the domain name and just the TLD and print
# Name: Grace Kulhanek
# Date: 02/03/2026

url = input("Enter the full URL: ")
cleanedURL = url.replace("https://", "")
print("Cleaned URL:", cleanedURL)

parts = cleanedURL.split(".")

domain = parts[1]
print("Domain:", domain)

TLD = parts[2]
TLDClean = TLD.strip("/")
# We might get a trailing/character, so we need to remove it
# TLDClean = TLD.replace("/", "")
print("Top-Level Domain:", TLDClean)


