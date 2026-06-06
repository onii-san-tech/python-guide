"""
Using a Custom Module

Now we import from the my_math.py file we created.
"""

import my_math

print(my_math.PI)
print(my_math.circle_area(10))
print(my_math.is_prime(23))

# Import specific functions
from my_math import celsius_to_fahrenheit, circle_perimeter

print(celsius_to_fahrenheit(100))
print(circle_perimeter(7))
