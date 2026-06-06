"""
Practice: Variables and Data Types

Complete the exercises below.
Each exercise builds on what you've learned so far.
"""

# Exercise 1: Create variables for your profile
# Replace the placeholders with real values
my_name = "Your Name"       # Change this!
my_age = 0                  # Change this!
my_height = 0.0             # Change this (in meters)!
is_student = True           # Change this!

print("=== My Profile ===")
print("Name:", my_name)
print("Age:", my_age)
print("Height:", my_height, "m")
print("Student:", is_student)

# Exercise 2: Calculate with variables
hourly_wage = 15.50
hours_worked = 40
weekly_pay = hourly_wage * hours_worked
print("\nWeekly pay: $" + str(weekly_pay))

# Exercise 3: Type checking
values = [42, 3.14, "Python", True, None]
for v in values:
    print(f"{v} is type: {type(v).__name__}")

# Exercise 4: User profile (runs interactively)
print("\n=== Create Your Profile ===")
name = input("Your name: ")
age = int(input("Your age: "))
print(f"Hi {name}! You'll be {age + 1} next birthday.")
