"""
What Are Exceptions?

An exception is an error that happens while the program runs.
Without handling, exceptions crash your program.
"""

# These would cause exceptions (commented out):
# print(10 / 0)           # ZeroDivisionError
# print(int("hello"))     # ValueError
# print(undefined_var)    # NameError
# my_list = [1, 2, 3]
# print(my_list[99])      # IndexError
# my_dict = {}
# print(my_dict["key"])   # KeyError
# open("nonexistent.txt") # FileNotFoundError

# Common built-in exceptions:
exceptions = {
    "ValueError":       "Wrong value type/format",
    "TypeError":        "Wrong type",
    "NameError":        "Variable doesn't exist",
    "IndexError":       "List index out of range",
    "KeyError":         "Dictionary key not found",
    "ZeroDivisionError":"Divided by zero",
    "FileNotFoundError":"File doesn't exist",
    "AttributeError":   "Object doesn't have attribute",
    "ImportError":      "Module not found",
    "StopIteration":    "Iterator exhausted",
}

print("Common Python Exceptions:")
for exc, desc in exceptions.items():
    print(f"  {exc}: {desc}")
