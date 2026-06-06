"""
Sets

A set is an unordered collection of UNIQUE values.
No duplicates allowed!
Use curly braces {} to create a set.
"""

# Creating a set
fruits = {"apple", "banana", "cherry", "apple"}  # duplicate removed
print(fruits)   # Order may vary!

# Creating from a list (removes duplicates)
numbers = list({3, 1, 4, 1, 5, 9, 2, 6, 5, 3})
print(sorted(numbers))  # [1, 2, 3, 4, 5, 6, 9]

# Adding and removing
s = {1, 2, 3}
s.add(4)
s.discard(2)      # Remove (no error if not found)
s.remove(3)       # Remove (error if not found)
print(s)

# Set operations
a = {1, 2, 3, 4, 5}
b = {4, 5, 6, 7, 8}

print(a | b)   # Union: all elements
print(a & b)   # Intersection: shared elements
print(a - b)   # Difference: in a but not b
print(a ^ b)   # Symmetric difference: in one but not both

# Membership check (very fast!)
vowels = {"a", "e", "i", "o", "u"}
print("a" in vowels)   # True
print("b" in vowels)   # False
