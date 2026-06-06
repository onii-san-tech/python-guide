"""
Try/Except

Try to run code. If an exception occurs, "except" catches it.
This prevents your program from crashing.
"""

# Basic try/except
try:
    result = 10 / 0
except ZeroDivisionError:
    print("Cannot divide by zero!")

# Handling multiple exceptions
def safe_parse(text):
    try:
        return int(text)
    except ValueError:
        print(f"'{text}' is not a valid integer.")
        return None

print(safe_parse("42"))       # 42
print(safe_parse("hello"))    # Error message, then None
print(safe_parse("3.14"))     # Error message, then None

# Catching multiple exception types
try:
    numbers = [1, 2, 3]
    print(numbers[10])   # IndexError
except (IndexError, KeyError) as e:
    print(f"Access error: {e}")

# Catch any exception (use sparingly!)
try:
    result = int("abc") + 1
except Exception as e:
    print(f"Something went wrong: {type(e).__name__}: {e}")
