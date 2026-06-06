"""
Dictionaries

A dictionary stores key-value pairs.
Like a real dictionary: look up a word (key) to get its meaning (value).
Keys must be unique.
"""

# Creating a dictionary
person = {
    "name": "Alice",
    "age": 30,
    "city": "New York"
}

print(person)
print(person["name"])   # Alice
print(person["age"])    # 30

# Adding/updating items
person["email"] = "alice@example.com"   # Add new key
person["age"] = 31                       # Update existing key
print(person)

# Safe access with .get()
print(person.get("phone", "No phone"))  # Returns default if key missing

# Removing items
removed = person.pop("city")     # Remove and return
print(f"Removed: {removed}")
del person["email"]              # Just delete
print(person)
