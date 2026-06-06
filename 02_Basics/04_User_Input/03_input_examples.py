"""
Practical Input Examples

Let's combine input with calculations to make useful mini programs.
"""

# Simple greeting
name = input("Enter your name: ")
city = input("Where are you from? ")
print(f"Nice to meet you, {name} from {city}!")

# Simple calculator
print("\n--- Simple Calculator ---")
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
print(f"{num1} + {num2} = {num1 + num2}")
print(f"{num1} - {num2} = {num1 - num2}")
print(f"{num1} * {num2} = {num1 * num2}")
if num2 != 0:
    print(f"{num1} / {num2} = {num1 / num2:.2f}")
