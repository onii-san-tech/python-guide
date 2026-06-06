"""
Common String Methods

Strings have many built-in methods for manipulation.
Methods are called with a dot: string.method()
"""

text = "  Hello, World!  "

# Case methods
print("python".upper())          # PYTHON
print("PYTHON".lower())          # python
print("hello world".title())     # Hello World
print("Hello World".swapcase())  # hELLO wORLD

# Whitespace methods
print(text.strip())              # "Hello, World!" (removes leading/trailing spaces)
print(text.lstrip())             # "Hello, World!  " (left only)
print(text.rstrip())             # "  Hello, World!" (right only)

# Find and check methods
sentence = "The quick brown fox"
print(sentence.find("quick"))   # 4 (index where "quick" starts)
print(sentence.count("the"))    # 0 (case-sensitive!)
print(sentence.count("the", 0, len(sentence)))  # still 0
print(sentence.lower().count("the"))  # 1

# Check methods (return True/False)
print("hello".startswith("he"))  # True
print("hello".endswith("lo"))    # True
print("12345".isdigit())         # True
print("hello".isalpha())         # True
print("hello123".isalnum())      # True
