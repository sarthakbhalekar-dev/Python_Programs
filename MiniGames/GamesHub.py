# Mini_Games/Games_Hub.py
import random

def games_menu():
    while True:
        print("\n=== MINI GAMES HUB ===")
        print("1. Number Guesser")
        print("2. Rock, Paper, Scissors")
        print("3. Interactive Story")
        print("0. Exit")
        
        choice = input("\nSelect a game (0-3): ").strip()
        
        if choice == "1":
            target = random.randint(1, 100)
            guess = None
            print("Guess the number between 1 and 100!")
            while guess != target:
                guess = int(input("Your guess: "))
                if guess < target: print("Higher!")
                elif guess > target: print("Lower!")
                else: print("🎉 Correct!")
                
        elif choice == "2":
            choices = ["rock", "paper", "scissors"]
            user = input("Choose rock, paper, or scissors: ").lower()
            bot = random.choice(choices)
            print(f"Bot chose: {bot}")
            if user == bot: print("It's a tie!")
            elif (user == "rock" and bot == "scissors") or \
                 (user == "paper" and bot == "rock") or \
                 (user == "scissors" and bot == "paper"):
                print(" You win!")
            else:
                print(" Bot wins!")
                
        elif choice == "3":
            name = input("Enter hero name: ")
            print(f"Once upon a time, {name} built a Python browser and conquered coding!")
            
        elif choice == "0":
            break

if __name__ == "__main__":
    games_menu()