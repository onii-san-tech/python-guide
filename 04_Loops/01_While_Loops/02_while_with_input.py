"""
While Loop with User Input

While loops are great for repeating until the user is done.
"""

# Keep asking until valid input
age = -1
while age < 0 or age > 120:
    age = int(input("Enter your age (0-120): "))

print(f"Your age is {age}. Valid!")

# Keep playing a game until user quits
print("\nNumber guessing game (type 'quit' to stop)")
secret = 42
while True:
    guess_str = input("Guess: ")
    if guess_str.lower() == "quit":
        print("Goodbye!")
        break
    guess = int(guess_str)
    if guess == secret:
        print("You got it!")
        break
    elif guess < secret:
        print("Too low!")
    else:
        print("Too high!")
