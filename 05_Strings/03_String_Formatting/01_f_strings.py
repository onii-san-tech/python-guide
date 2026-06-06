"""
F-Strings (Formatted String Literals)

F-strings let you embed variables and expressions directly in strings.
They're the modern, recommended way to format strings in Python.
"""

name = "Alice"
age = 30
score = 92.567

# Basic f-string: prefix with f, put variables in {}
print(f"Hello, {name}!")
print(f"You are {age} years old.")

# Expressions inside {}
print(f"Next year you'll be {age + 1}.")
print(f"Double your score: {score * 2}")

# Formatting numbers
print(f"Score: {score:.2f}")     # 2 decimal places: 92.57
print(f"Score: {score:.0f}")     # 0 decimal places: 93
print(f"Big: {1000000:,}")       # With commas: 1,000,000
print(f"Percent: {0.85:.1%}")    # As percent: 85.0%

# Padding and alignment
print(f"{'left':<10}|")    # left-aligned, width 10
print(f"{'right':>10}|")   # right-aligned
print(f"{'center':^10}|")  # centered
