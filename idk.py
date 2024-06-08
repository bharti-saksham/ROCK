import random

def get_user_choice():
    choice = input("Enter 'rock', 'paper', or 'scissors': ").lower()
    while choice not in ['rock', 'paper', 'scissors']:
        print("Invalid choice! Please enter 'rock', 'paper', or 'scissors'.")
        choice = input("Enter 'rock', 'paper', or 'scissors': ").lower()
    return choice

def get_computer_choice():
    return random.choice(['rock', 'paper', 'scissors'])

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == 'rock' and computer_choice == 'scissors') or \
         (user_choice == 'paper' and computer_choice == 'rock') or \
         (user_choice == 'scissors' and computer_choice == 'paper'):
        return "You win!"
    else:
        return "Computer wins!"

def main():
    num_games = int(input("How many games do you want to play? "))
    user_wins = 0
    computer_wins = 0
    
    for _ in range(num_games):
        user_choice = get_user_choice()
        computer_choice = get_computer_choice()
        print(f"You chose {user_choice}. Computer chose {computer_choice}.")
        result = determine_winner(user_choice, computer_choice)
        print(result)
        
        if result == "You win!":
            user_wins += 1
        elif result == "Computer wins!":
            computer_wins += 1
    
    print(f"Final Score - You: {user_wins}, Computer: {computer_wins}")

if __name__ == "__main__":
    main()
