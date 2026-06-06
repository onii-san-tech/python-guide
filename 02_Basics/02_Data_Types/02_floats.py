"""
Floats (float)

Floats are decimal numbers.
Use them when you need precision (like money, height, or measurements).
"""

# Float examples
price = 9.99
temperature = 36.6
pi = 3.14159

print(price)
print(temperature)
print(pi)

# Float math
print(0.1 + 0.2)  # Shows floating point quirk: 0.30000000000000004
print(round(0.1 + 0.2, 2))  # Fix it with round(): 0.3

# Mixing int and float: result is always float
print(5 + 2.0)   # 7.0
print(10 / 2)    # 5.0 (regular division always gives float)
print(10 // 2)   # 5 (integer division gives int)
