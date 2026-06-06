"""
List Slicing

Slicing extracts a portion of a list.
Same syntax as string slicing.
"""

numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

print(numbers[2:5])    # [2, 3, 4]
print(numbers[:4])     # [0, 1, 2, 3]
print(numbers[6:])     # [6, 7, 8, 9]
print(numbers[::2])    # [0, 2, 4, 6, 8] every 2nd
print(numbers[::-1])   # Reversed list

# Copying a list
original = [1, 2, 3]
copy = original[:]  # Creates a real copy
copy.append(4)
print(original)  # [1, 2, 3] — unchanged!
print(copy)      # [1, 2, 3, 4]
