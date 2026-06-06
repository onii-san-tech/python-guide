"""
Logical Operators: and, or, not

Logical operators combine multiple conditions.
"""

age = 20
has_id = True

# AND: both conditions must be True
can_enter = age >= 18 and has_id
print(can_enter)  # True

# OR: at least one condition must be True
is_weekend = False
is_holiday = True
day_off = is_weekend or is_holiday
print(day_off)  # True

# NOT: flips True to False, False to True
is_raining = False
go_outside = not is_raining
print(go_outside)  # True

# Combining them
score = 85
attendance = 90
passes = score >= 60 and attendance >= 75
print("Passes:", passes)  # True
