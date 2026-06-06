"""
Practice: Functions

Build reusable functions for these exercises.
"""

# Exercise 1: Temperature conversion functions
def celsius_to_fahrenheit(c):
    return c * 9/5 + 32

def fahrenheit_to_celsius(f):
    return (f - 32) * 5/9

def celsius_to_kelvin(c):
    return c + 273.15

print("=== Temperature Converter ===")
temp = float(input("Enter temperature in Celsius: "))
print(f"{temp}°C = {celsius_to_fahrenheit(temp):.1f}°F")
print(f"{temp}°C = {celsius_to_kelvin(temp):.1f}K")

# Exercise 2: Statistics functions
def get_mean(numbers):
    return sum(numbers) / len(numbers)

def get_median(numbers):
    sorted_nums = sorted(numbers)
    n = len(sorted_nums)
    mid = n // 2
    if n % 2 == 0:
        return (sorted_nums[mid - 1] + sorted_nums[mid]) / 2
    return sorted_nums[mid]

data = [10, 20, 30, 40, 50, 60, 15]
print(f"\nData: {data}")
print(f"Mean: {get_mean(data):.2f}")
print(f"Median: {get_median(data)}")
print(f"Min: {min(data)}, Max: {max(data)}")

# Exercise 3: Greeting card generator
def make_card(name, occasion, message="Wishing you all the best!"):
    width = 40
    print("*" * width)
    print(f"*{'Happy ' + occasion:^{width-2}}*")
    print(f"*{'Dear ' + name + ',':^{width-2}}*")
    print(f"*{message:^{width-2}}*")
    print("*" * width)

make_card("Alice", "Birthday")
make_card("Bob", "Anniversary", "May your love grow stronger!")
