"""
Practice: Loops

Master loops with these exercises.
"""

# Exercise 1: Sum of numbers 1 to 100
total = 0
for i in range(1, 101):
    total += i
print(f"Sum of 1 to 100 = {total}")

# Exercise 2: FizzBuzz (classic interview problem)
print("\nFizzBuzz (1 to 20):")
for n in range(1, 21):
    if n % 15 == 0:
        print("FizzBuzz")
    elif n % 3 == 0:
        print("Fizz")
    elif n % 5 == 0:
        print("Buzz")
    else:
        print(n)

# Exercise 3: Countdown
print("\nCountdown:")
for i in range(10, 0, -1):
    print(i)
print("Blast off!")

# Exercise 4: Find all even numbers from user input
print("\nEven number finder:")
limit = int(input("Enter a limit: "))
evens = []
for n in range(1, limit + 1):
    if n % 2 == 0:
        evens.append(n)
print("Even numbers:", evens)
