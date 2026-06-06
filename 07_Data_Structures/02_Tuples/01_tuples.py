"""
Tuples

A tuple is like a list but IMMUTABLE — you can't change it after creation.
Use parentheses () instead of brackets [].
Use tuples for data that shouldn't change.
"""

# Creating tuples
point = (3, 5)
rgb = (255, 128, 0)
single = (42,)    # Single element tuple — note the comma!
empty = ()

print(point)
print(rgb)

# Accessing (same as lists)
print(point[0])   # 3
print(point[-1])  # 5

# Tuples are immutable
# point[0] = 99  <- This would cause a TypeError!

# Unpacking
x, y = point
print(f"x={x}, y={y}")

red, green, blue = rgb
print(f"R={red}, G={green}, B={blue}")

# Tuples can be used as dictionary keys (lists cannot!)
locations = {(40.7, -74.0): "New York", (51.5, -0.1): "London"}
print(locations[(40.7, -74.0)])

# Named tuples (more readable)
from collections import namedtuple
Person = namedtuple("Person", ["name", "age", "city"])
alice = Person("Alice", 30, "NYC")
print(alice.name, alice.age, alice.city)
