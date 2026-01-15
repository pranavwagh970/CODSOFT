import random

def play_game():
    print("--- Rock-Paper-Scissors ---")
    options = ["rock", "paper", "scissors"]
    
    while True:
        user_choice = input("Choose rock, paper, or scissors (or 'quit' to stop): ").lower()
        
        if user_choice == 'quit':
            break
        if user_choice not in options:
            print("Invalid choice. Try again.")
            continue

        computer_choice = random.choice(options)
        print(f"You chose: {user_choice}")
        print(f"Computer chose: {computer_choice}")

        if user_choice == computer_choice:
            print("It's a tie!")
        elif (user_choice == "rock" and computer_choice == "scissors") or \
             (user_choice == "scissors" and computer_choice == "paper") or \
             (user_choice == "paper" and computer_choice == "rock"):
            print("You win!")
        else:
            print("You lose!")
        
        play_again = input("Play another round? (y/n): ").lower()
        if play_again != 'y':
            break

if __name__ == "__main__":
    play_game()
