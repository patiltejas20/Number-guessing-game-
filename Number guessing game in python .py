import random

def play_game():
    print("=== 🎲 Number Guessing Game ===")
    print("I have chosen a number between 1 and 100. Can you guess it?")
    
    number = random.randint(1, 100)
    attempts = 0
    
    while True:
        try:
            guess = int(input("Enter your guess: "))
            attempts += 1
            
            if guess < number:
                print("📉 Too low! Try again.")
            elif guess > number:
                print("📈 Too high! Try again.")
            else:
                print(f"🎉 Correct! The number was {number}.")
                print(f"You guessed it in {attempts} attempts.")
                break
        except ValueError:
            print("⚠ Please enter a valid number.")

def main():
    while True:
        play_game()
        again = input("Do you want to play again? (y/n): ").lower()
        if again != "y":
            print("👋 Thanks for playing!")
            break

if __name__ == "__main__":
    main()
