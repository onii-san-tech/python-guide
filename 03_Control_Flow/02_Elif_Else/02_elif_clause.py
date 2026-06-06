"""
Elif Clause

elif means "else if" — check another condition if the first was False.
You can chain as many elif clauses as you need.
"""

score = 85

if score >= 90:
    print("Grade: A")
elif score >= 80:
    print("Grade: B")
elif score >= 70:
    print("Grade: C")
elif score >= 60:
    print("Grade: D")
else:
    print("Grade: F")

# Another example: time of day greeting
hour = 14  # 2 PM (24-hour clock)

if hour < 12:
    print("Good morning!")
elif hour < 17:
    print("Good afternoon!")
elif hour < 21:
    print("Good evening!")
else:
    print("Good night!")
