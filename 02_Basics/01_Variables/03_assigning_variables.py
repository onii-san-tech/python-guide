"""
Assigning Variables

Assignment means putting a value into a variable.
The = sign is the assignment operator.
"""

# Simple assignment
x = 10
y = 20

# Assign the result of math
total = x + y
print(total)  # 30

# Assign one variable to another
a = 5
b = a  # b gets the same value as a
print(a, b)  # 5 5

# Multiple assignment on one line
p, q, r = 1, 2, 3
print(p, q, r)  # 1 2 3

# Assign same value to multiple variables
cat = dog = bird = "pet"
print(cat, dog, bird)  # pet pet pet

# Update a variable using itself
count = 0
count = count + 1
print(count)  # 1

count += 1  # Shorthand for count = count + 1
print(count)  # 2
