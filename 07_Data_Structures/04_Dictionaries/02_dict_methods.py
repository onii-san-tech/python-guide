"""
Dictionary Methods

Useful methods for working with dictionaries.
"""

student = {
    "name": "Bob",
    "grade": "A",
    "score": 95,
    "subject": "Math"
}

# Getting keys, values, and both
print(list(student.keys()))     # ['name', 'grade', 'score', 'subject']
print(list(student.values()))   # ['Bob', 'A', 95, 'Math']
print(list(student.items()))    # [('name', 'Bob'), ...]

# Looping
for key in student:
    print(f"{key}: {student[key]}")

for key, value in student.items():
    print(f"{key} => {value}")

# Checking for keys
print("name" in student)    # True
print("phone" in student)   # False

# Merging dictionaries
extra = {"club": "Chess", "sport": "Tennis"}
student.update(extra)
print(student)

# Dictionary from two lists
keys = ["a", "b", "c"]
values = [1, 2, 3]
combined = dict(zip(keys, values))
print(combined)
