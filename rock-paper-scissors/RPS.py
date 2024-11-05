import random

# Dictionary to map choices to emojis
emoji = {'r': '🪨', 'p': '📰', 's': '✂️'}
choices = ('r', 'p', 's')

while True:
    # Prompt user for their choice
    ur = input("Rock, Paper, or Scissors? (r/p/s): ").lower()
    if ur not in choices:
        print("Invalid choice! Please enter 'r', 'p', or 's'.")
        continue
    
    # Computer randomly selects an option
    cmp = random.choice(choices)

    # Display choices with emojis
    print(f"You: {emoji[ur]}")
    print(f"Computer: {emoji[cmp]}")

    # Determine the result
    if ur == cmp:
        print("It's a Tie!")
    elif (ur == 'r' and cmp == 's') or (ur == 's' and cmp == 'p') or (ur == 'p' and cmp == 'r'):
        print("You win! 🏆")
    else:
        print("You lose. 😔")

    # Ask if the player wants to continue
    ans = input("Do you want to play again? (y/n): ").lower()
    if ans == 'n':
        print("Thanks for playing!")
        break
