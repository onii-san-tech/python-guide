"""
Variable Scope

Scope determines where a variable can be accessed.
Variables created inside a function are "local" — only usable inside.
Variables created outside functions are "global".
"""

# Global variable
x = 10

def show_x():
    print(x)  # Can read global variable

show_x()  # 10

# Local variable
def make_local():
    y = 99   # This only exists inside this function
    print(y)

make_local()  # 99
# print(y)    # Would cause NameError! y doesn't exist here.

# Local variable shadows global
name = "Global Alice"

def test_scope():
    name = "Local Bob"  # This is a NEW local variable
    print(name)         # Local Bob

test_scope()
print(name)   # Global Alice — unchanged!

# To modify a global, use the global keyword (use sparingly!)
counter = 0

def increment():
    global counter
    counter += 1

increment()
increment()
print(counter)  # 2
