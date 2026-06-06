"""
Project 2: Number Guessing Game

The computer picks a secret number.
The player tries to guess it with hints.
"""

import random
import time

def get_difficulty():
    print("\n🎮 Choose difficulty:")
    print("  1. Easy   (1–50,  10 guesses)")
    print("  2. Medium (1–100, 7 guesses)")
    print("  3. Hard   (1–200, 5 guesses)")
    
    while True:
        choice = input("Your choice (1/2/3): ").strip()
        if choice == "1":
            return 50, 10, "Easy"
        elif choice == "2":
            return 100, 7, "Medium"
        elif choice == "3":
            return 200, 5, "Hard"
        else:
            print("Please choose 1, 2, or 3.")

def get_hint(guess, secret):
    diff = abs(guess - secret)
    if diff == 0:
        return "🎯 Exactly right!"
    elif diff <= 5:
        hint = "🔥 Burning hot!"
    elif diff <= 15:
        hint = "♨️  Very warm"
    elif diff <= 30:
        hint = "😐 Lukewarm"
    elif diff <= 50:
        hint = "❄️  Cold"
    else:
        hint = "🧊 Freezing!"
    
    direction = "📉 Go lower" if guess > secret else "📈 Go higher"
    return f"{hint} — {direction}"

def play_game():
    high, max_guesses, level = get_difficulty()
    secret = random.randint(1, high)
    guesses = []
    start_time = time.time()
    
    print(f"\n🎲 I'm thinking of a number between 1 and {high}.")
    print(f"You have {max_guesses} guesses. Good luck!\n")
    
    for attempt in range(1, max_guesses + 1):
        remaining = max_guesses - attempt + 1
        print(f"Guess #{attempt}/{max_guesses} ({remaining} remaining):")
        
        while True:
            try:
                guess = int(input(f"Your guess (1-{high}): "))
                if 1 <= guess <= high:
                    break
                print(f"Please guess between 1 and {high}.")
            except ValueError:
                print("Please enter a whole number.")
        
        guesses.append(guess)
        
        if guess == secret:
            elapsed = time.time() - start_time
            print(f"\n🎉 Correct! The number was {secret}!")
            print(f"You got it in {attempt} guess(es) in {elapsed:.1f} seconds!")
            
            # Score
            score = max(0, (max_guesses - attempt + 1) * 100 // max_guesses)
            print(f"Score: {score}/100")
            return True
        else:
            hint = get_hint(guess, secret)
            print(hint)
    
    print(f"\n💔 Out of guesses! The secret number was {secret}.")
    print(f"Your guesses: {guesses}")
    return False

def main():
    print("=" * 40)
    print("   🎮 NUMBER GUESSING GAME 🎮")
    print("=" * 40)
    
    wins = 0
    losses = 0
    
    while True:
        won = play_game()
        if won:
            wins += 1
        else:
            losses += 1
        
        print(f"\n📊 Score: {wins} wins, {losses} losses")
        
        again = input("\nPlay again? (y/n): ").strip().lower()
        if again != "y":
            print("\nThanks for playing! Goodbye! 👋")
            break

if __name__ == "__main__":
    main()
