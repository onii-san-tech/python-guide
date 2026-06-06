"""
Debugging Tips

Debugging means finding and fixing bugs (errors) in your code.
Here are practical techniques.
"""

# Technique 1: Print debugging
def calculate_average(numbers):
    print(f"DEBUG: Input = {numbers}")  # Check input
    total = sum(numbers)
    print(f"DEBUG: Total = {total}")    # Check intermediate value
    avg = total / len(numbers)
    print(f"DEBUG: Average = {avg}")    # Check result
    return avg

result = calculate_average([10, 20, 30, 40])
print(f"Average: {result}")

# Technique 2: Using assert for sanity checks
def get_discount(price, percent):
    assert 0 <= percent <= 100, f"Percent must be 0-100, got {percent}"
    assert price >= 0, f"Price must be non-negative, got {price}"
    return price * (percent / 100)

print(get_discount(100, 20))   # 20.0

try:
    get_discount(100, 150)     # Will trigger assertion!
except AssertionError as e:
    print(f"Assertion failed: {e}")

# Technique 3: Reading tracebacks
# When Python shows an error, read from bottom to top:
# Last line: the actual error
# Lines above: where it came from (call stack)

# Technique 4: Using breakpoints (interactive debugging)
# Add this line where you want to pause execution:
# import pdb; pdb.set_trace()
# Or in Python 3.7+: breakpoint()
# Then: n (next), s (step into), c (continue), p variable (print value)

print("\nDebugging techniques demonstrated!")
