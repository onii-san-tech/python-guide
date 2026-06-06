"""
Dictionary and Set Comprehensions

The comprehension syntax also works for dicts and sets.
"""

# Dict comprehension
squares = {n: n**2 for n in range(1, 6)}
print(squares)  # {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

# From two lists
names = ["Alice", "Bob", "Charlie"]
scores = [95, 88, 72]
grade_book = {name: score for name, score in zip(names, scores)}
print(grade_book)

# Filtering in dict comprehension
passing = {name: score for name, score in grade_book.items() if score >= 80}
print(passing)

# Set comprehension
even_set = {n for n in range(20) if n % 2 == 0}
print(even_set)  # Unique even numbers

# Practical: invert a dictionary
original = {"a": 1, "b": 2, "c": 3}
inverted = {v: k for k, v in original.items()}
print(inverted)  # {1: 'a', 2: 'b', 3: 'c'}
