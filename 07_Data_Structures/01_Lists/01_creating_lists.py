"""
Lists

A list stores multiple values in order.
Lists are mutable — you can change them after creation.
"""

# Creating lists
fruits = ["apple", "banana", "cherry"]
numbers = [1, 2, 3, 4, 5]
mixed = [1, "hello", True, 3.14, None]   # Lists can hold different types
empty = []

print(fruits)
print(numbers)
print(mixed)

# Accessing items (indexing)
print(fruits[0])   # apple
print(fruits[-1])  # cherry (last)

# Length
print(len(fruits))  # 3
