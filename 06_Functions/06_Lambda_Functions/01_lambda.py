"""
Lambda Functions

A lambda is a small, anonymous (unnamed) function.
Useful for short, simple operations.
"""

# Regular function
def square(x):
    return x ** 2

# Equivalent lambda
square_lambda = lambda x: x ** 2

print(square(5))        # 25
print(square_lambda(5)) # 25

# Lambda with multiple parameters
add = lambda a, b: a + b
print(add(3, 4))  # 7

# Lambdas are great with built-in functions like sorted, map, filter
numbers = [3, 1, 4, 1, 5, 9, 2, 6]

# Sort by ascending value
sorted_nums = sorted(numbers)
print(sorted_nums)

# Sort a list of dicts by a specific key
people = [
    {"name": "Charlie", "age": 30},
    {"name": "Alice", "age": 25},
    {"name": "Bob", "age": 35},
]
by_age = sorted(people, key=lambda p: p["age"])
for person in by_age:
    print(person)
