# An example of creating and using your own function
# Name: Grace Kulhanek
# Date: 01/22/2026

import datetime

def greet(name):
   """"This function greets the person whose name is passed in. In addition we want to print a welcome message that includes the day of the week."""
   message = "Hello" + " " + name + "!"
   x = datetime.datetime.now()
   dayOfWeek = x.strftime("%A")
   return message + " Happy " + dayOfWeek + "!"

userName = input("Please enter your name: ")
greetingMessage = greet(userName)
print(greetingMessage)