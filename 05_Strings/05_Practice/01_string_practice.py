"""
Practice: Strings

Master string operations with these exercises.
"""

# Exercise 1: Reverse a string
text = input("Enter a word: ")
reversed_text = text[::-1]
print(f"Reversed: {reversed_text}")
is_palindrome = text.lower() == reversed_text.lower()
print(f"Is palindrome: {is_palindrome}")

# Exercise 2: Word counter
sentence = input("Enter a sentence: ")
words = sentence.split()
word_count = len(words)
char_count = len(sentence.replace(" ", ""))
print(f"Words: {word_count}")
print(f"Characters (no spaces): {char_count}")

# Exercise 3: Title formatter
raw_name = input("Enter a full name (all lowercase): ")
formatted = raw_name.strip().title()
initials = ".".join([part[0].upper() for part in raw_name.split()]) + "."
print(f"Formatted name: {formatted}")
print(f"Initials: {initials}")

# Exercise 4: Password validator
password = input("Enter a password: ")
has_upper = any(c.isupper() for c in password)
has_lower = any(c.islower() for c in password)
has_digit = any(c.isdigit() for c in password)
long_enough = len(password) >= 8

print(f"\nPassword analysis:")
print(f"  Has uppercase: {has_upper}")
print(f"  Has lowercase: {has_lower}")
print(f"  Has digit: {has_digit}")
print(f"  At least 8 chars: {long_enough}")
print(f"  Strong password: {all([has_upper, has_lower, has_digit, long_enough])}")
