"""
Nested If Statements

You can put if statements inside other if statements.
This lets you check multiple levels of conditions.
"""

age = 20
has_ticket = True

if age >= 18:
    print("Age check passed.")
    if has_ticket:
        print("You may enter!")
    else:
        print("You need a ticket.")
else:
    print("You must be 18 or older.")

# Theme park ride example
height = 140  # cm
health_ok = True

if height >= 120:
    if health_ok:
        print("Enjoy the ride!")
    else:
        print("Health conditions prevent you from riding.")
else:
    print("You must be at least 120cm tall.")
