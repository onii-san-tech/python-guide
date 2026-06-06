"""
Recursion

A recursive function calls itself.
It must have a "base case" to stop recursion.
Great for problems that can be divided into smaller versions of themselves.
"""

# Factorial: n! = n * (n-1) * (n-2) * ... * 1
def factorial(n):
    # Base case: stop recursion
    if n <= 1:
        return 1
    # Recursive case: call itself with a smaller value
    return n * factorial(n - 1)

print(factorial(5))   # 120 = 5*4*3*2*1
print(factorial(10))  # 3628800

# Fibonacci: each number is the sum of the two before it
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

for i in range(10):
    print(fibonacci(i), end=" ")
print()
# 0 1 1 2 3 5 8 13 21 34

# Countdown using recursion
def countdown(n):
    if n <= 0:
        print("Blast off!")
        return
    print(n)
    countdown(n - 1)

countdown(5)
