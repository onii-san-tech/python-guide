"""
Converting Input to Numbers

Since input() returns strings, convert them to numbers when you need math.
Use int() for whole numbers and float() for decimals.
"""

# Convert to integer
age_str = input("Enter your age: ")
age = int(age_str)
print("Next year you'll be:", age + 1)

# Convert to float
price_str = input("Enter item price: ")
price = float(price_str)
tax = price * 0.1
print(f"With 10% tax: ${price + tax:.2f}")

# Shortcut: convert right inside input()
year = int(input("Enter birth year: "))
print("You are approximately", 2024 - year, "years old.")
