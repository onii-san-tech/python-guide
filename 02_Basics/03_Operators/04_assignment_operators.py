"""
Assignment Operators

Assignment operators are shortcuts for updating variables.
Instead of writing x = x + 1, you can write x += 1.
"""

x = 10

x += 5   # Same as: x = x + 5
print(x)  # 15

x -= 3   # Same as: x = x - 3
print(x)  # 12

x *= 2   # Same as: x = x * 2
print(x)  # 24

x //= 4  # Same as: x = x // 4
print(x)  # 6

x **= 2  # Same as: x = x ** 2
print(x)  # 36

x %= 10  # Same as: x = x % 10
print(x)  # 6

# Very common in real code:
counter = 0
counter += 1  # increment
counter += 1
counter += 1
print(counter)  # 3
