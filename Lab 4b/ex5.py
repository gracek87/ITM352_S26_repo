# Ask for a sentence from the user (using input())
# Turn the sentence into a list of strings. 
# Reverse the list.  Join the reversed list back into a string.
# Name: Grace Kulhanek
# Date: 02/03/2026

sentence = input("Enter a sentence: ")

#1. Turn the sentence into a list of words.
words = sentence.split(" ")
print("List of words:", words)

#2. Reverse the list.
words.reverse()
print("Reversed list of words:", words)

#3. Join the reversed list back into a string.
newSentence = " ".join(words)
print("Reversed sentence:", newSentence)

