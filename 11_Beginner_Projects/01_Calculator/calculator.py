"""
Project 1: Calculator

A full-featured command-line calculator.
Supports basic arithmetic and some advanced operations.
"""

import math

def add(a, b): return a + b
def subtract(a, b): return a - b
def multiply(a, b): return a * b
def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero!")
    return a / b
def power(a, b): return a ** b
def modulo(a, b): return a % b
def square_root(a):
    if a < 0:
        raise ValueError("Cannot take square root of negative number!")
    return math.sqrt(a)

def show_menu():
    print("\n╔════════════════════════╗")
    print("║    Python Calculator    ║")
    print("╠════════════════════════╣")
    print("║  1. Addition (+)       ║")
    print("║  2. Subtraction (-)    ║")
    print("║  3. Multiplication (*) ║")
    print("║  4. Division (/)       ║")
    print("║  5. Power (**)         ║")
    print("║  6. Modulo (%)         ║")
    print("║  7. Square Root (√)    ║")
    print("║  8. History            ║")
    print("║  9. Quit               ║")
    print("╚════════════════════════╝")

def get_number(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Please enter a valid number.")

def format_number(n):
    """Remove unnecessary decimal places."""
    return int(n) if n == int(n) else round(n, 6)

def main():
    history = []
    
    print("Welcome to the Python Calculator!")
    
    while True:
        show_menu()
        choice = input("Choose an option (1-9): ").strip()
        
        if choice == "9":
            print("Goodbye!")
            break
        
        if choice == "8":
            if history:
                print("\n📜 Calculation History:")
                for i, entry in enumerate(history[-10:], 1):  # Last 10
                    print(f"  {i}. {entry}")
            else:
                print("No history yet.")
            continue
        
        if choice not in "1234567":
            print("Invalid choice. Try again.")
            continue
        
        try:
            if choice == "7":
                a = get_number("Enter number: ")
                result = square_root(a)
                expression = f"√{format_number(a)} = {format_number(result)}"
            else:
                a = get_number("Enter first number: ")
                b = get_number("Enter second number: ")
                
                operations = {
                    "1": (add, "+"),
                    "2": (subtract, "-"),
                    "3": (multiply, "×"),
                    "4": (divide, "÷"),
                    "5": (power, "^"),
                    "6": (modulo, "%"),
                }
                
                func, symbol = operations[choice]
                result = func(a, b)
                expression = f"{format_number(a)} {symbol} {format_number(b)} = {format_number(result)}"
            
            print(f"\n✅ Result: {format_number(result)}")
            history.append(expression)
            
        except ValueError as e:
            print(f"\n❌ Error: {e}")

if __name__ == "__main__":
    main()
