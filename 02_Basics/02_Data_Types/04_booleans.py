"""
Booleans (bool)

Booleans have only two values: True or False.
They are used to represent yes/no, on/off, correct/incorrect.
"""

# Boolean values (capital T and F are required!)
is_raining = True
is_sunny = False

print(is_raining)
print(is_sunny)

# Comparisons produce booleans
print(5 > 3)    # True
print(5 < 3)    # False
print(5 == 5)   # True (== checks equality)
print(5 != 3)   # True (not equal)
print(5 >= 5)   # True
print(5 <= 4)   # False

# Booleans in real use
age = 20
is_adult = age >= 18
print("Is adult:", is_adult)

score = 75
passed = score >= 60
print("Passed:", passed)
