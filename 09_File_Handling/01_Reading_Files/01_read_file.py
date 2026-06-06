"""
Reading Files

Python can read and write files on your computer.
Always use the with statement — it automatically closes the file.
"""

import os

# First, create a sample file to read
sample_path = "sample.txt"
with open(sample_path, "w") as f:
    f.write("Hello, File!\n")
    f.write("Line 2\n")
    f.write("Line 3\n")

# Read the entire file at once
with open(sample_path, "r") as file:
    content = file.read()
    print(content)

# Read line by line
with open(sample_path, "r") as file:
    for line in file:
        print(line.strip())  # strip() removes the newline

# Read all lines into a list
with open(sample_path, "r") as file:
    lines = file.readlines()
    print(lines)

# Clean up
os.remove(sample_path)
