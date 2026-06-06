"""
File Modes

Different modes control how you can use a file.
"""

# "r" - Read only (default). Error if file doesn't exist.
# "w" - Write only. Creates or overwrites.
# "a" - Append. Creates or adds to end.
# "r+" - Read and write.
# "x" - Create. Error if file already exists.
# "b" - Binary mode (add to other modes: "rb", "wb")

# Example: safe file creation
filename = "new_file.txt"

try:
    with open(filename, "x") as f:  # exclusive creation
        f.write("This file was just created!")
    print("File created!")
except FileExistsError:
    print(f"{filename} already exists!")

# Reading binary files (images, etc.)
# with open("image.png", "rb") as f:
#     data = f.read()
#     print(f"File size: {len(data)} bytes")

import os
if os.path.exists(filename):
    os.remove(filename)
