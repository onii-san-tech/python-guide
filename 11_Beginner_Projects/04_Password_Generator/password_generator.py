"""
Project 4: Password Generator

Generates secure random passwords with customizable options.
"""

import random
import string

def generate_password(length=12, use_upper=True, use_lower=True, 
                       use_digits=True, use_symbols=True):
    """Generate a random password with specified requirements."""
    
    charset = ""
    required = []
    
    if use_lower:
        charset += string.ascii_lowercase
        required.append(random.choice(string.ascii_lowercase))
    if use_upper:
        charset += string.ascii_uppercase
        required.append(random.choice(string.ascii_uppercase))
    if use_digits:
        charset += string.digits
        required.append(random.choice(string.digits))
    if use_symbols:
        symbols = "!@#$%^&*()_+-=[]{}|;:,.<>?"
        charset += symbols
        required.append(random.choice(symbols))
    
    if not charset:
        raise ValueError("At least one character type must be selected!")
    
    # Fill the rest of the password
    remaining_length = length - len(required)
    password = required + [random.choice(charset) for _ in range(remaining_length)]
    
    # Shuffle to avoid predictable patterns
    random.shuffle(password)
    return "".join(password)

def check_strength(password):
    """Rate password strength."""
    score = 0
    feedback = []
    
    if len(password) >= 12: score += 2
    elif len(password) >= 8: score += 1
    else: feedback.append("Too short (< 8 chars)")
    
    if any(c.isupper() for c in password): score += 1
    else: feedback.append("Add uppercase letters")
    
    if any(c.islower() for c in password): score += 1
    else: feedback.append("Add lowercase letters")
    
    if any(c.isdigit() for c in password): score += 1
    else: feedback.append("Add numbers")
    
    if any(c in "!@#$%^&*()_+-=[]{}|;:,.<>?" for c in password): score += 2
    else: feedback.append("Add special characters")
    
    if score >= 6: strength = "Very Strong 💪"
    elif score >= 5: strength = "Strong ✅"
    elif score >= 3: strength = "Medium ⚠️"
    else: strength = "Weak ❌"
    
    return strength, feedback

def main():
    print("=" * 45)
    print("    🔐 SECURE PASSWORD GENERATOR")
    print("=" * 45)
    
    while True:
        print("\nOptions:")
        print("  1. Generate password")
        print("  2. Generate multiple passwords")
        print("  3. Check password strength")
        print("  4. Quit")
        
        choice = input("\nChoice: ").strip()
        
        if choice == "1":
            try:
                length = int(input("Password length [12]: ").strip() or "12")
                upper = input("Uppercase letters? (y/n) [y]: ").lower() != "n"
                lower = input("Lowercase letters? (y/n) [y]: ").lower() != "n"
                digits = input("Numbers? (y/n) [y]: ").lower() != "n"
                symbols = input("Symbols? (y/n) [y]: ").lower() != "n"
                
                password = generate_password(length, upper, lower, digits, symbols)
                strength, tips = check_strength(password)
                
                print(f"\n🔑 Generated password: {password}")
                print(f"💪 Strength: {strength}")
                if tips:
                    print("💡 Tips:", ", ".join(tips))
                    
            except ValueError as e:
                print(f"Error: {e}")
        
        elif choice == "2":
            count = int(input("How many passwords? [5]: ").strip() or "5")
            length = int(input("Length each? [16]: ").strip() or "16")
            
            print(f"\n{'#':3} {'Password':20} {'Strength':15}")
            print("-" * 40)
            for i in range(1, count + 1):
                pwd = generate_password(length)
                strength, _ = check_strength(pwd)
                print(f"{i:3}. {pwd:20} {strength}")
        
        elif choice == "3":
            password = input("Enter password to check: ")
            strength, tips = check_strength(password)
            print(f"Strength: {strength}")
            if tips:
                print("Suggestions:")
                for tip in tips:
                    print(f"  • {tip}")
        
        elif choice == "4":
            print("Goodbye! Stay secure! 🔒")
            break

if __name__ == "__main__":
    main()
