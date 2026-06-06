"""
String Slicing

Slicing lets you grab a portion of a string.
Syntax: string[start:stop:step]
"""

text = "Hello, World!"
#       0123456789...

print(text[0:5])    # Hello  (index 0 up to, not including, 5)
print(text[7:12])   # World
print(text[:5])     # Hello  (start defaults to 0)
print(text[7:])     # World! (end defaults to last)
print(text[:])      # Hello, World! (full copy)
print(text[-6:-1])  # World
print(text[::2])    # Hlo ol! (every 2nd character)
print(text[::-1])   # !dlroW ,olleH (reversed!)

# Practical uses
filename = "document_report.pdf"
extension = filename[-3:]   # pdf
basename = filename[:-4]    # document_report
print(extension, basename)
