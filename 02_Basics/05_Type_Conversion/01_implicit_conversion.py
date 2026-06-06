"""
Implicit Type Conversion

Python automatically converts types in some situations.
This happens without you asking for it.
"""

# Int + Float = Float
result = 5 + 2.0
print(result)       # 7.0
print(type(result)) # <class 'float'>

# Int * Float = Float
result2 = 3 * 1.5
print(result2)      # 4.5

# Boolean is treated as 0 (False) or 1 (True)
print(True + 1)     # 2
print(False + 10)   # 10
print(True * 5)     # 5
