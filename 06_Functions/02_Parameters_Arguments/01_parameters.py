"""
Parameters and Arguments

Parameters let you pass information INTO a function.
The function can then use that information.
"""

# Function with one parameter
def greet(name):
    print(f"Hello, {name}!")

greet("Alice")
greet("Bob")
greet("Charlie")

# Function with multiple parameters
def add(a, b):
    print(f"{a} + {b} = {a + b}")

add(3, 5)
add(10, 20)
add(100, 200)

# The names inside () are "parameters"
# The values you pass when calling are "arguments"
