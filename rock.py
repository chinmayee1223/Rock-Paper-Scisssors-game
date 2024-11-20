import random

def get_computer_choice():
    """Generate the computer's choice randomly."""
    choices = ['rock', 'paper', 'scissors']
    return random.choice(choices)

def determine_winner(user_choice, computer_choice):
    """Determine the winner of the game based on the rules."""
    if user_choice == computer_choice:
        return "It's a tie!"
    
    if (user_choice == 'rock' and computer_choice == 'scissors') or \
       (user_choice == 'scissors' and computer_choice == 'paper') or \
       (user_choice == 'paper' and computer_choice == 'rock'):
        return "You win!"
    else:
        return "You lose!"

def play_game():
    """Main function to play the Rock, Paper, Scissors game."""
    user_score = 0
    computer_score = 0
    
    while True:
        print("\nWelcome to Rock, Paper, Scissors!")
        print("Please choose one: rock, paper, or scissors.")
        
        # User Input
        user_choice = input("Your choice: ").lower()
        while user_choice not in ['rock', 'paper', 'scissors']:
            print("Invalid choice! Please choose 'rock', 'paper', or 'scissors'.")
            user_choice = input("Your choice: ").lower()

        # Computer Selection
        computer_choice = get_computer_choice()
        
        # Display the choices
        print(f"\nYou chose: {user_choice}")
        print(f"The computer chose: {computer_choice}")
        
        # Determine the winner
        result = determine_winner(user_choice, computer_choice)
        print(result)
        
        # Update scores based on the result
        if result == "You win!":
            user_score += 1
        elif result == "You lose!":
            computer_score += 1

        # Display the score
        print(f"Your score: {user_score}")
        print(f"Computer's score: {computer_score}")
        
        # Ask the user if they want to play again
        play_again = input("\nDo you want to play again? (yes/no): ").lower()
        if play_again != 'yes':
            print("\nThanks for playing! Goodbye!")
            break

if __name__ == "__main__":
    play_game()

