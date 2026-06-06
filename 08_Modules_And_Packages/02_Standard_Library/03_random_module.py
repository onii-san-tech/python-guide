"""
The random Module

Generate random numbers, make random choices.
"""

import random

# Random float between 0 and 1
print(random.random())

# Random integer between a and b (inclusive)
print(random.randint(1, 10))

# Random float in range
print(random.uniform(1.0, 5.0))

# Random choice from a list
fruits = ["apple", "banana", "cherry", "date"]
print(random.choice(fruits))

# Multiple random choices
print(random.choices(fruits, k=3))  # With replacement
print(random.sample(fruits, 3))     # Without replacement

# Shuffle a list
deck = list(range(1, 14))  # Cards 1-13
random.shuffle(deck)
print(deck)

# Reproducible randomness (seed)
random.seed(42)
print(random.randint(1, 100))  # Always same result with same seed
