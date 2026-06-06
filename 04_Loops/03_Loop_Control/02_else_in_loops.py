"""
Else in Loops

Python allows an else clause on loops.
The else block runs only if the loop completed without hitting break.
"""

# Search for a value
numbers = [1, 3, 5, 7, 9]
target = 6

for num in numbers:
    if num == target:
        print(f"Found {target}!")
        break
else:
    print(f"{target} not found in the list.")

# Practical: checking if a number is prime
n = 17
for divisor in range(2, int(n**0.5) + 1):
    if n % divisor == 0:
        print(f"{n} is NOT prime (divisible by {divisor})")
        break
else:
    print(f"{n} IS prime!")
