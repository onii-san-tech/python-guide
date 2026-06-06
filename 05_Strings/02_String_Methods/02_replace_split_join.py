"""
Replace, Split, and Join

Three of the most useful string methods.
"""

# replace()
text = "I love cats. Cats are great!"
new_text = text.replace("cats", "dogs").replace("Cats", "Dogs")
print(new_text)

# split() - splits a string into a list
sentence = "apple,banana,cherry,date"
fruits = sentence.split(",")
print(fruits)           # ['apple', 'banana', 'cherry', 'date']
print(fruits[0])        # apple

words = "Hello World Python".split()  # splits on whitespace by default
print(words)

# join() - joins a list of strings into one string
items = ["one", "two", "three"]
result = ", ".join(items)
print(result)           # one, two, three

words_list = ["Python", "is", "awesome"]
sentence = " ".join(words_list)
print(sentence)         # Python is awesome
