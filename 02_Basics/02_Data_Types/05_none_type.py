"""
NoneType (None)

None represents "nothing" or "no value".
It's useful when a variable exists but has no value yet.
"""

# None represents the absence of a value
result = None
print(result)        # None
print(type(result))  # <class 'NoneType'>

# Often used as a placeholder
user_name = None

# Later, you might assign a real value
user_name = "Alice"
print(user_name)

# Checking for None
value = None
print(value is None)     # True
print(value is not None) # False

# Functions that don't return anything return None
def greet():
    print("Hello!")

output = greet()   # prints "Hello!"
print(output)      # None  (greet() returns nothing)
