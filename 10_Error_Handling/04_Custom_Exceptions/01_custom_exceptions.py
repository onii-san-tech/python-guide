"""
Custom Exceptions

You can create your own exception types.
Inherit from Exception (or a more specific exception).
"""

# Define a custom exception
class InvalidAgeError(Exception):
    """Raised when an invalid age is provided."""
    def __init__(self, age, message="Age must be between 0 and 150"):
        self.age = age
        self.message = message
        super().__init__(f"{message}. Got: {age}")

class InsufficientFundsError(Exception):
    """Raised when a bank account has insufficient funds."""
    def __init__(self, amount, balance):
        self.amount = amount
        self.balance = balance
        super().__init__(
            f"Cannot withdraw ${amount:.2f}. Balance is ${balance:.2f}"
        )

# Using custom exceptions
def set_age(age):
    if not isinstance(age, int):
        raise TypeError("Age must be an integer")
    if age < 0 or age > 150:
        raise InvalidAgeError(age)
    return age

def withdraw(balance, amount):
    if amount > balance:
        raise InsufficientFundsError(amount, balance)
    return balance - amount

# Test them
try:
    set_age(-5)
except InvalidAgeError as e:
    print(f"Error: {e}")

try:
    new_balance = withdraw(100.0, 200.0)
except InsufficientFundsError as e:
    print(f"Error: {e}")

try:
    age = set_age(25)
    print(f"Age set to {age}")
except (InvalidAgeError, TypeError) as e:
    print(f"Error: {e}")
