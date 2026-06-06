"""
Nested Loops

A loop inside another loop.
The inner loop completes fully for each iteration of the outer loop.
"""

# Multiplication table
for i in range(1, 4):       # outer: 1, 2, 3
    for j in range(1, 4):   # inner: 1, 2, 3
        print(f"{i} x {j} = {i*j}")
    print("---")

# Pattern printing
rows = 5
for row in range(1, rows + 1):
    print("*" * row)
