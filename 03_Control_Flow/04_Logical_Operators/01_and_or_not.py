"""
Logical Operators in Conditions

Use and, or, not to combine conditions.
This avoids deeply nested if statements.
"""

# AND: both must be True
age = 25
has_license = True

if age >= 16 and has_license:
    print("You can drive!")

# OR: at least one must be True
is_member = False
has_coupon = True

if is_member or has_coupon:
    print("You get a discount!")

# NOT: flips the condition
is_closed = False

if not is_closed:
    print("The store is open.")

# Combining multiple conditions
username = "admin"
password = "secret123"
is_active = True

if username == "admin" and password == "secret123" and is_active:
    print("Login successful!")
else:
    print("Login failed.")
