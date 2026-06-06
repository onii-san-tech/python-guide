"""
CSV Files

CSV (Comma-Separated Values) is a simple format for storing data.
Each line is a row; values are separated by commas.
"""

import csv
import os

# Writing a CSV file
students = [
    ["Name", "Age", "Grade"],
    ["Alice", 20, "A"],
    ["Bob", 22, "B"],
    ["Charlie", 21, "A+"],
]

with open("students.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerows(students)

print("CSV written!")

# Reading a CSV file
print("\nReading CSV:")
with open("students.csv", "r") as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)

# Using DictReader (each row becomes a dict)
print("\nAs dictionaries:")
with open("students.csv", "r") as file:
    reader = csv.DictReader(file)
    for row in reader:
        print(f"{row['Name']}: {row['Grade']}")

os.remove("students.csv")
