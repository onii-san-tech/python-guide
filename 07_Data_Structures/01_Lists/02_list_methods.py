"""
List Methods

Lists have many built-in methods for adding, removing, and modifying items.
"""

fruits = ["apple", "banana", "cherry"]

# Adding items
fruits.append("date")          # Add to end
fruits.insert(1, "blueberry")  # Insert at position 1
print(fruits)

# Removing items
fruits.remove("banana")   # Remove by value (first occurrence)
popped = fruits.pop()     # Remove and return last item
popped2 = fruits.pop(0)   # Remove and return item at index 0
print(fruits)
print("Popped:", popped, popped2)

# Other methods
numbers = [3, 1, 4, 1, 5, 9, 2, 6]
numbers.sort()                  # Sort in place
print(numbers)
numbers.reverse()               # Reverse in place
print(numbers)
print(numbers.count(1))         # Count occurrences
print(numbers.index(5))         # Find index of value

# Combining lists
list1 = [1, 2, 3]
list2 = [4, 5, 6]
combined = list1 + list2         # Creates new list
list1.extend(list2)              # Adds list2 to list1 in place
print(list1)
