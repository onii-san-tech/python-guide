"""
Default Arguments

You can give parameters default values.
If the caller doesn't provide a value, the default is used.
"""

# greeting has a default value
def greet(name, greeting="Hello"):
    print(f"{greeting}, {name}!")

greet("Alice")              # Uses default: Hello, Alice!
greet("Bob", "Good morning")  # Override default: Good morning, Bob!
greet("Carol", greeting="Hi") # Named argument: Hi, Carol!

# Power function with default exponent
def power(base, exponent=2):
    return base ** exponent

print(power(3))     # 9  (3 squared)
print(power(3, 3))  # 27 (3 cubed)
print(power(2, 10)) # 1024

# IMPORTANT: Default arguments must come AFTER non-default ones
# def bad(a=1, b):  <- Error!
# def good(a, b=1): <- OK!
