"""
*args and **kwargs

*args lets a function accept any number of positional arguments.
**kwargs lets a function accept any number of keyword arguments.
"""

# *args: collect extra positional arguments into a tuple
def add_all(*numbers):
    total = 0
    for num in numbers:
        total += num
    return total

print(add_all(1, 2, 3))          # 6
print(add_all(1, 2, 3, 4, 5))    # 15
print(add_all(10))                # 10

# **kwargs: collect extra keyword arguments into a dict
def show_info(**details):
    for key, value in details.items():
        print(f"  {key}: {value}")

show_info(name="Alice", age=30, city="NYC")

# Combining both
def describe(title, *items, **options):
    print(f"\n{title}:")
    for item in items:
        print(f"  - {item}")
    for key, val in options.items():
        print(f"  [{key}={val}]")

describe("Fruits", "apple", "banana", "cherry", sorted=True, count=3)
