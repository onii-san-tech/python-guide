"""
The sys Module

Access Python interpreter information and system-specific parameters.
"""

import sys

# Python version
print(sys.version)
print(sys.version_info)

# Platform
print(sys.platform)  # 'linux', 'darwin', 'win32'

# Command line arguments
print("Script name:", sys.argv[0])
print("All arguments:", sys.argv)

# Exit the program (don't run this in the middle of a script!)
# sys.exit(0)  # 0 = success, any other = error

# Recursion limit
print("Max recursion depth:", sys.getrecursionlimit())
sys.setrecursionlimit(2000)  # Can increase if needed

# Path where Python searches for modules
import pprint
pprint.pprint(sys.path[:3])  # Show first 3 paths
