"""
Return Values

Functions can send back a result using return.
The result can be stored in a variable.
"""

# Function that returns a value
def add(a, b):
    return a + b

result = add(3, 5)
print(result)  # 8

# Use the return value directly
print(add(10, 20))  # 30

# Return from calculations
def celsius_to_fahrenheit(celsius):
    return celsius * 9/5 + 32

temp_f = celsius_to_fahrenheit(100)
print(f"100°C = {temp_f}°F")

# Returning multiple values
def min_max(numbers):
    return min(numbers), max(numbers)

low, high = min_max([3, 1, 4, 1, 5, 9, 2, 6])
print(f"Min: {low}, Max: {high}")
