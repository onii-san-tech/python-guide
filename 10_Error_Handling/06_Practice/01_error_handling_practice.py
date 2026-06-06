"""
Practice: Error Handling

Build robust programs that handle errors gracefully.
"""

# Exercise 1: Safe calculator
def safe_calculator():
    print("=== Safe Calculator ===")
    print("Operations: +, -, *, /")
    
    while True:
        try:
            num1 = float(input("First number: "))
            op = input("Operation (+, -, *, /): ")
            num2 = float(input("Second number: "))
            
            if op == "+":
                result = num1 + num2
            elif op == "-":
                result = num1 - num2
            elif op == "*":
                result = num1 * num2
            elif op == "/":
                if num2 == 0:
                    raise ZeroDivisionError("Cannot divide by zero")
                result = num1 / num2
            else:
                raise ValueError(f"Unknown operator: {op}")
            
            print(f"Result: {result}")
            
        except ValueError as e:
            print(f"Invalid input: {e}")
        except ZeroDivisionError as e:
            print(f"Math error: {e}")
        
        again = input("Calculate again? (y/n): ")
        if again.lower() != "y":
            break

safe_calculator()
