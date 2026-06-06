"""
Explicit Type Conversion

You can manually convert between types using conversion functions.
This is called "casting" or "type conversion".
"""

# Convert to integer
print(int(3.9))       # 3 (truncates, doesn't round!)
print(int("42"))      # 42
print(int(True))      # 1
print(int(False))     # 0

# Convert to float
print(float(5))       # 5.0
print(float("3.14"))  # 3.14

# Convert to string
print(str(42))        # "42"
print(str(3.14))      # "3.14"
print(str(True))      # "True"

# Convert to boolean
print(bool(0))        # False
print(bool(1))        # True
print(bool(""))       # False (empty string)
print(bool("hello"))  # True  (non-empty string)
print(bool(None))     # False

# Practical use
age_text = "25"
age_number = int(age_text)
print(age_number + 5)  # 30
