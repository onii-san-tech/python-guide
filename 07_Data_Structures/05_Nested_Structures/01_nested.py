"""
Nested Data Structures

Lists can contain lists. Dicts can contain dicts.
You can mix and nest them as deeply as needed.
"""

# List of lists
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print(matrix[0][0])   # 1 (row 0, col 0)
print(matrix[1][2])   # 6 (row 1, col 2)

# Print the matrix
for row in matrix:
    print(row)

# Dictionary with lists
school = {
    "name": "Python Academy",
    "students": ["Alice", "Bob", "Charlie"],
    "grades": {"Alice": 95, "Bob": 88, "Charlie": 72}
}

print(school["name"])
print(school["students"][0])           # Alice
print(school["grades"]["Bob"])         # 88

# List of dictionaries (very common pattern!)
products = [
    {"id": 1, "name": "Laptop", "price": 999.99},
    {"id": 2, "name": "Mouse", "price": 29.99},
    {"id": 3, "name": "Keyboard", "price": 79.99},
]

for product in products:
    print(f"[{product['id']}] {product['name']}: ${product['price']}")
