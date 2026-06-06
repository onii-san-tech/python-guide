"""
Practice: Data Structures

Put your data structure knowledge to the test.
"""

# Exercise 1: Shopping cart
print("=== Shopping Cart ===")
cart = []

while True:
    action = input("Add item (or 'done'): ")
    if action.lower() == "done":
        break
    price = float(input(f"Price of {action}: $"))
    cart.append({"item": action, "price": price})

print("\nYour cart:")
total = 0
for i, entry in enumerate(cart, 1):
    print(f"  {i}. {entry['item']}: ${entry['price']:.2f}")
    total += entry["price"]
print(f"Total: ${total:.2f}")

# Exercise 2: Word frequency counter
print("\n=== Word Frequency ===")
sentence = input("Enter a sentence: ")
words = sentence.lower().split()
freq = {}
for word in words:
    freq[word] = freq.get(word, 0) + 1

# Sort by frequency
sorted_freq = sorted(freq.items(), key=lambda x: x[1], reverse=True)
for word, count in sorted_freq:
    print(f"  '{word}': {count}")

# Exercise 3: Unique characters
text = input("Enter text: ")
unique_chars = sorted(set(text.replace(" ", "")))
print(f"Unique characters: {unique_chars}")
print(f"Count: {len(unique_chars)}")
