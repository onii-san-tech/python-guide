"""
Break and Continue

break: exits the loop immediately
continue: skips the rest of this iteration and goes to the next
"""

# break example: stop when you find what you want
numbers = [3, 7, 2, 9, 1, 5]

print("Looking for 9...")
for num in numbers:
    if num == 9:
        print("Found 9! Stopping.")
        break
    print(num)

print()

# continue example: skip certain items
print("Printing odd numbers only:")
for num in range(1, 11):
    if num % 2 == 0:  # if even
        continue       # skip it
    print(num)
