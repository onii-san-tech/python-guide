"""
Importing Modules

A module is a file containing Python code.
import lets you use code from other files.
"""

# Import a whole module
import math

print(math.pi)           # 3.141592653589793
print(math.sqrt(16))     # 4.0
print(math.floor(3.7))   # 3
print(math.ceil(3.2))    # 4
print(math.pow(2, 8))    # 256.0

# Import specific items from a module
from math import pi, sqrt, factorial

print(pi)           # Can use directly without math.
print(sqrt(25))     # 5.0
print(factorial(5)) # 120

# Import with alias
import math as m
print(m.sin(m.pi / 2))  # 1.0

from datetime import datetime as dt
now = dt.now()
print(now)
