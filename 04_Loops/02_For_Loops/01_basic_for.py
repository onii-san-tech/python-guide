"""
For Loops

A for loop goes through each item in a sequence.
It's perfect when you know exactly what to loop over.
"""

# Loop over a list
fruits = ["apple", "banana", "cherry"]

for fruit in fruits:
    print(fruit)

# Loop over a string (character by character)
for letter in "Python":
    print(letter)

# Loop with range()
for i in range(5):      # 0, 1, 2, 3, 4
    print(i)

for i in range(1, 6):   # 1, 2, 3, 4, 5
    print(i)

for i in range(0, 10, 2):  # 0, 2, 4, 6, 8 (step of 2)
    print(i)
