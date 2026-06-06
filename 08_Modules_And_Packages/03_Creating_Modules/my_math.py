"""
my_math.py — A Custom Module

This is a module we created ourselves.
Other Python files can import from this file.
"""

PI = 3.14159265358979

def circle_area(radius):
    """Calculate the area of a circle."""
    return PI * radius ** 2

def circle_perimeter(radius):
    """Calculate the perimeter (circumference) of a circle."""
    return 2 * PI * radius

def is_prime(n):
    """Check if a number is prime."""
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def celsius_to_fahrenheit(celsius):
    """Convert Celsius to Fahrenheit."""
    return celsius * 9/5 + 32

if __name__ == "__main__":
    # This block only runs when the file is run directly,
    # NOT when it's imported by another file.
    print("Testing my_math module:")
    print(f"Circle area (r=5): {circle_area(5):.2f}")
    print(f"Is 17 prime? {is_prime(17)}")
