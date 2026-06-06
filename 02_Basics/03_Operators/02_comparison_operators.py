"""
Comparison Operators

Comparison operators compare two values.
They always return True or False.
"""

x = 10
y = 5

print(x == y)  # Equal to:              False
print(x != y)  # Not equal to:          True
print(x > y)   # Greater than:          True
print(x < y)   # Less than:             False
print(x >= y)  # Greater than or equal: True
print(x <= y)  # Less than or equal:    False

# Comparing strings
print("apple" == "apple")  # True
print("apple" == "Apple")  # False (case matters!)
print("apple" < "banana")  # True (alphabetical order)

# Comparing with variables
age = 18
print(age >= 18)  # True - is adult
print(age == 21)  # False - not 21
