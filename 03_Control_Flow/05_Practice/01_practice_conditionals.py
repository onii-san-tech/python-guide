"""
Practice: Control Flow

Work through these exercises to master if/elif/else.
"""

# Exercise 1: Number classifier
print("=== Number Classifier ===")
num = float(input("Enter a number: "))

if num > 0:
    print("Positive")
elif num < 0:
    print("Negative")
else:
    print("Zero")

# Exercise 2: Password strength checker
print("\n=== Password Strength ===")
password = input("Enter a password: ")
length = len(password)

if length >= 12:
    strength = "Strong"
elif length >= 8:
    strength = "Medium"
elif length >= 4:
    strength = "Weak"
else:
    strength = "Too Short"

print(f"Password strength: {strength}")

# Exercise 3: Simple login
print("\n=== Login System ===")
USERNAME = "pythonlearner"
PASSWORD = "ilovecode"

entered_user = input("Username: ")
entered_pass = input("Password: ")

if entered_user == USERNAME and entered_pass == PASSWORD:
    print("Welcome! Login successful.")
else:
    print("Invalid credentials. Access denied.")
