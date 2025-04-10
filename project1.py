import random

def game_winner(user, computer):

    if user == computer:
        return "tie"
    elif (user == "snake" and computer == "water") or \
         (user == "water" and computer == "gun") or \
         (user == "gun" and computer == "snake"):
        return "user"
    else:
        return "computer"

def play_game():
    user_score = 0
    computer_score = 0
    
    while True:
        print("\nChoose: snake, water, gun and quit")
        user_choice = input("Your choice: ").lower()
        
        if user_choice == "quit":
            break
            
        if user_choice not in ["snake", "water", "gun"]:
            print("Invalid choice! Try again.")
            continue
            
        computer_choice = random.choice(["snake", "water", "gun"])
        print(f"Computer chose: {computer_choice}")
        
        result = game_winner(user_choice, computer_choice) 
        
        if result == "user":
            user_score += 1
            print("You win!")
        elif result == "computer":
            computer_score += 1
            print("Computer wins!")
        else:
            print("It's a tie!")
            
        print(f"Score - You: {user_score}, Computer: {computer_score}")
    
    print("\nGame Over!")
    print(f"Final Score - You: {user_score}, Computer: {computer_score}")

play_game()