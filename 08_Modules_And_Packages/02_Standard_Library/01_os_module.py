"""
The os Module

os provides functions for interacting with the operating system.
"""

import os

# Current directory
print(os.getcwd())

# List files in a directory
files = os.listdir(".")
for f in files[:5]:
    print(f)

# Check if path exists
print(os.path.exists("README.md"))

# Join paths safely
path = os.path.join("folder", "subfolder", "file.txt")
print(path)  # folder/subfolder/file.txt (or \ on Windows)

# Get file info
script_path = os.path.abspath(__file__)
print("Script location:", script_path)
print("Directory:", os.path.dirname(script_path))
print("Filename:", os.path.basename(script_path))

# Environment variables
home = os.environ.get("HOME", "Unknown")
print("Home directory:", home)
