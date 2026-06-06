"""
Operator Precedence

Python follows rules about which operations happen first.
Remember: Parentheses > Exponents > Multiply/Divide > Add/Subtract
"""

# Without parentheses
print(2 + 3 * 4)     # 14 (multiply first)
print(10 - 2 ** 3)   # 2  (exponent first: 2^3=8, then 10-8=2)
print(10 / 2 + 3)    # 8.0 (divide first: 10/2=5, then 5+3=8)

# With parentheses (override defaults)
print((2 + 3) * 4)   # 20 (add first)
print((10 - 2) ** 3) # 512 (subtract first: 8^3=512)
print(10 / (2 + 3))  # 2.0 (add first: 2+3=5, then 10/5=2)

# When in doubt, use parentheses to be clear!
total = (price := 9.99) * (quantity := 3)
print(f"3 items at $9.99 = ${9.99 * 3}")
