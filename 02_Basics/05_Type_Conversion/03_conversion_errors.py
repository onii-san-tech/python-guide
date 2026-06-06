"""
Conversion Errors

Not all conversions are possible.
Converting an invalid value causes a ValueError.
"""

# This works:
print(int("42"))   # Fine!

# These cause errors (commented out to prevent crashing):
# print(int("hello"))  # ValueError: invalid literal for int()
# print(float("abc"))  # ValueError: could not convert string to float
# print(int("3.14"))   # ValueError: int() can't convert a float string directly

# Safe conversion: convert float string via float first
text = "3.14"
number = int(float(text))  # works! Goes: "3.14" -> 3.14 -> 3
print(number)  # 3

# Always validate user input before converting!
user_input = "not_a_number"
try:
    value = int(user_input)
except ValueError:
    print("That's not a valid number!")
