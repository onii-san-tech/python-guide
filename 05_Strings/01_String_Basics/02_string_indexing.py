"""
String Indexing

Each character in a string has a position (index).
Python starts counting from 0, not 1.
Negative indexes count from the end.
"""

word = "Python"
#       P y t h o n
# Index: 0 1 2 3 4 5
# Neg:  -6-5-4-3-2-1

print(word[0])   # P (first character)
print(word[1])   # y
print(word[5])   # n (last character)
print(word[-1])  # n (last from the end)
print(word[-2])  # o (second from the end)
print(word[-6])  # P (same as word[0])

# Length of a string
print(len(word))  # 6
