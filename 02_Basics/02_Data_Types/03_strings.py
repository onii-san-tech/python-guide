"""
Strings (str)

Strings are text.
Anything inside quotes is a string.
You can use single or double quotes.
"""

# Creating strings
greeting = "Hello, World!"
name = 'Alice'

print(greeting)
print(name)

# Strings can contain letters, numbers, and symbols
message = "I am 25 years old!"
print(message)

# Combining strings (concatenation)
first = "Good"
second = "Morning"
full = first + " " + second
print(full)  # Good Morning

# Repeating strings
line = "-" * 20
print(line)  # --------------------

# Getting the length of a string
print(len("Hello"))  # 5
print(len(greeting))

# Strings are case-sensitive
print("hello" == "Hello")  # False
print("hello" == "hello")  # True
