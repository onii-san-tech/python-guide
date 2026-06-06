"""
The .format() Method

The older way to format strings.
Still used in many codebases.
"""

# Basic usage
print("Hello, {}!".format("Alice"))
print("I am {} years old.".format(25))

# Multiple values
print("{} + {} = {}".format(3, 4, 7))

# Named placeholders
print("Name: {name}, Age: {age}".format(name="Bob", age=30))

# Reusing values
print("{0} says hello to {1}. {1} says hi to {0}.".format("Alice", "Bob"))

# Formatting numbers
pi = 3.14159
print("Pi is approximately {:.2f}".format(pi))
