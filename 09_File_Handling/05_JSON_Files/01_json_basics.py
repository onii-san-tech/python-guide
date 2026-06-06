"""
JSON Files

JSON (JavaScript Object Notation) is a popular format for storing structured data.
Python dicts and lists map naturally to JSON.
"""

import json
import os

# Python dict to JSON string
person = {
    "name": "Alice",
    "age": 30,
    "hobbies": ["reading", "coding"],
    "address": {
        "city": "NYC",
        "zip": "10001"
    }
}

# Write to JSON file
with open("person.json", "w") as file:
    json.dump(person, file, indent=4)   # indent makes it readable

print("JSON file written!")

# Read from JSON file
with open("person.json", "r") as file:
    loaded = json.load(file)

print(loaded["name"])
print(loaded["hobbies"])
print(loaded["address"]["city"])

# Convert between string and dict
json_string = json.dumps(person)    # dict -> string
back_to_dict = json.loads(json_string)  # string -> dict
print(type(json_string), type(back_to_dict))

os.remove("person.json")
