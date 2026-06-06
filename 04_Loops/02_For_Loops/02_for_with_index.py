"""
For Loops with Index

Sometimes you need both the item and its position.
Use enumerate() to get both.
"""

colors = ["red", "green", "blue"]

# Without enumerate (manual index)
for i in range(len(colors)):
    print(i, colors[i])

print()

# With enumerate (Pythonic!)
for index, color in enumerate(colors):
    print(f"Color {index}: {color}")

print()

# Start counting from 1
for i, color in enumerate(colors, start=1):
    print(f"{i}. {color}")
