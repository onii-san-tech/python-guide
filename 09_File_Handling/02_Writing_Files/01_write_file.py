"""
Writing Files

Use "w" mode to write (overwrites existing content).
Use "a" mode to append (adds to existing content).
"""

# Writing to a file (creates it if it doesn't exist)
with open("diary.txt", "w") as file:
    file.write("Day 1: Started learning Python.\n")
    file.write("Day 2: Learned about files.\n")

# Appending to the file
with open("diary.txt", "a") as file:
    file.write("Day 3: Getting better every day!\n")

# Writing multiple lines at once
lines = ["Line A\n", "Line B\n", "Line C\n"]
with open("multi_line.txt", "w") as file:
    file.writelines(lines)

# Read back what we wrote
with open("diary.txt", "r") as file:
    print(file.read())

# Cleanup
import os
os.remove("diary.txt")
os.remove("multi_line.txt")
