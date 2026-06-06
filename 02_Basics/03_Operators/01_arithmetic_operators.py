"""
Arithmetic Operators

Arithmetic operators do math on numbers.
They work just like in regular math class.
"""

a = 10
b = 3

print(a + b)   # Addition:       13
print(a - b)   # Subtraction:    7
print(a * b)   # Multiplication: 30
print(a / b)   # Division:       3.3333...
print(a // b)  # Floor Division: 3  (drops the decimal)
print(a % b)   # Modulo:         1  (remainder after division)
print(a ** b)  # Exponent:       1000 (10 to the power of 3)

# Order of operations (PEMDAS/BODMAS)
result = 2 + 3 * 4
print(result)  # 14, not 20! Multiplication happens first.

result = (2 + 3) * 4
print(result)  # 20, parentheses go first.
