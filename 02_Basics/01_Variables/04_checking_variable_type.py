"""
Checking Variable Types

Every variable has a type.
The type tells Python what kind of data is stored.
Use type() to check the type of any variable.
"""

name = "Alice"
age = 25
height = 5.7
is_student = True

print(type(name))       # <class 'str'>    - text
print(type(age))        # <class 'int'>    - whole number
print(type(height))     # <class 'float'>  - decimal number
print(type(is_student)) # <class 'bool'>   - True or False

# You can print type and value together
print(f"name is {type(name).__name__}: {name}")
print(f"age is {type(age).__name__}: {age}")
