"""
Finally and Else in Try/Except

else: runs if NO exception occurred
finally: ALWAYS runs, no matter what (great for cleanup)
"""

def divide(a, b):
    try:
        result = a / b
    except ZeroDivisionError:
        print("Error: division by zero!")
        return None
    else:
        # This runs only if no exception happened
        print(f"Success! {a} / {b} = {result}")
        return result
    finally:
        # This ALWAYS runs (exception or not)
        print("divide() finished.")

divide(10, 2)
print()
divide(10, 0)

# Real-world use: ensuring a file gets closed
print("\nFile example:")
filename = "temp.txt"
with open(filename, "w") as f:
    f.write("test")

try:
    file = open(filename, "r")
    content = file.read()
    result = int(content)   # This will fail (content is "test")
except ValueError as e:
    print(f"Value error: {e}")
finally:
    file.close()  # Always close, even if error occurred
    print("File closed.")
    
import os
os.remove(filename)
