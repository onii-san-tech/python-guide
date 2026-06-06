"""
Creating Strings

Strings are sequences of characters enclosed in quotes.
Python is flexible: single, double, or triple quotes all work.
"""

# Single quotes
name = 'Alice'

# Double quotes
greeting = "Hello, World!"

# Triple quotes (for multi-line strings)
poem = """
Roses are red,
Violets are blue,
Python is great,
And so are you!
"""

print(name)
print(greeting)
print(poem)

# Use one type of quote inside the other
message1 = "It's a beautiful day"
message2 = 'She said "Hello!"'
print(message1)
print(message2)

# Escape characters
print("Line 1\nLine 2")       # \n = newline
print("Name:\tAlice")         # \t = tab
print("She said \"Hi!\"")     # \" = literal quote
print("Back\\slash")          # \\ = literal backslash
