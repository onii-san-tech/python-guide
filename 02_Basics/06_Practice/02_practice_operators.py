"""
Practice: Operators

Work through these exercises to practice operators.
"""

# Exercise 1: Basic arithmetic
print("=== Arithmetic Practice ===")
a, b = 17, 5
print(f"{a} + {b} = {a + b}")
print(f"{a} - {b} = {a - b}")
print(f"{a} * {b} = {a * b}")
print(f"{a} / {b} = {a / b}")
print(f"{a} // {b} = {a // b}")
print(f"{a} % {b} = {a % b}")
print(f"{a} ** {b} = {a ** b}")

# Exercise 2: Is a number even or odd?
number = int(input("\nEnter a number: "))
is_even = number % 2 == 0
print(f"{number} is even: {is_even}")

# Exercise 3: Temperature converter
celsius = float(input("Enter temperature in Celsius: "))
fahrenheit = celsius * 9/5 + 32
print(f"{celsius}°C = {fahrenheit:.1f}°F")

# Exercise 4: Simple interest
principal = float(input("Principal amount ($): "))
rate = float(input("Interest rate (% per year): "))
years = int(input("Number of years: "))
interest = principal * (rate / 100) * years
print(f"Simple interest: ${interest:.2f}")
print(f"Total amount: ${principal + interest:.2f}")
