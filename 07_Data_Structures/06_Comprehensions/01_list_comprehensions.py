"""
List Comprehensions

A concise way to create lists.
Often replaces a for loop + append pattern.
"""

# Traditional way:
squares_old = []
for n in range(1, 6):
    squares_old.append(n ** 2)

# List comprehension way:
squares = [n ** 2 for n in range(1, 6)]
print(squares)  # [1, 4, 9, 16, 25]

# With condition (filtering)
evens = [n for n in range(20) if n % 2 == 0]
print(evens)

# Transform strings
fruits = ["apple", "banana", "cherry"]
upper_fruits = [f.upper() for f in fruits]
print(upper_fruits)

# Filtering and transforming
words = ["hello", "world", "python", "code", "fun"]
long_words = [w.capitalize() for w in words if len(w) > 4]
print(long_words)

# Nested comprehension (creates 2D list)
grid = [[row * col for col in range(1, 4)] for row in range(1, 4)]
for row in grid:
    print(row)
