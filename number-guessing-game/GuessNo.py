import random

# Generate a random number between 1 and 100
rNo = random.randint(1, 100)

while True:
    try:
        # Prompt user to guess the number
        aNo = int(input("Guess a number between 1 and 100: "))
        
        # Check if the guess is too high, too low, or correct
        if aNo > rNo:
            print("Too high!")
        elif aNo < rNo:
            print("Too low!")
        else:
            print("Congrats!! You guessed it right!")
            break
    except ValueError:
        # Handle non-integer input
        print("Please enter a valid number.")
