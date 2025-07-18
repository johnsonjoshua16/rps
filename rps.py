print("Rock, Paper, Scissors!") #title of the game

import random
import time

choices = ["rock", "paper", "scissors"] # List of valid choices

def play_rps():
    user_choice = input("Enter rock, paper, or scissors: ").strip().lower()
    while user_choice not in choices:
        print("Invalid choice. Please enter rock, paper, or scissors.") # Validate user input
        user_choice = input("Enter rock, paper, or scissors: ").strip().lower()

    computer_choice = random.choice(choices)
    print(f"Computer chose: {computer_choice}") # Display computer's choice

    # Determine the outcome

    if user_choice == computer_choice: 
        print("It's a tie!")
        # Check for a tie
    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "paper" and computer_choice == "rock") or \
         (user_choice == "scissors" and computer_choice == "paper"):
             # Check for a win
        print("You win!")
    else:
        # If not a tie or win, then it's a loss
        print("You lose!")

while True:
    play_rps()
    time.sleep(1)  # Pause for 1 second before asking to play again
    again = input("Do you want to play again? (yes/no): ").strip().lower()
    while again not in ["yes", "no"]:
        print("Invalid input. Please enter yes or no.")
        again = input("Do you want to play again? (yes/no): ").strip().lower()
    if again != "yes":
        print("Thanks for playing!")
        break

