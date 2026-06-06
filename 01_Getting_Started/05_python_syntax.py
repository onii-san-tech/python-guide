"""
Python Syntax Rules

Python has some simple rules you must follow.
Breaking these rules causes errors.
"""

# Rule 1: Indentation matters!
# (We'll see this more with if/loops, but just know it's important)

# Rule 2: Python is case-sensitive
# "Name" and "name" are DIFFERENT things
name = "Alice"
Name = "Bob"   # This is a DIFFERENT variable!
print(name)    # Alice
print(Name)    # Bob

# Rule 3: Strings need quotes
print("This works")
print('This also works')

# Rule 4: No spaces in variable names
# good_name = "ok"     <- correct
# bad name = "error"   <- would cause an error!

# Rule 5: Each statement goes on its own line
print("Line 1")
print("Line 2")

print("Python is easy to read!")
