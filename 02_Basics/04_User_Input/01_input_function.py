"""
Getting Input from Users

The input() function pauses the program and waits for the user to type something.
Whatever the user types is returned as a string.
"""

# Basic input
name = input("What is your name? ")
print("Hello,", name)

# input() always returns a string!
age = input("How old are you? ")
print("You are", age, "years old.")
print("Type of age:", type(age))  # <class 'str'> - it's text, not a number!
