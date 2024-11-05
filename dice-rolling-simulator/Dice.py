import random

while True:
    Q = input("Do you want to roll a dice (Y/N): ")
    if Q.lower() == "y":
        dice1 = random.randint(1, 6)
        dice2 = random.randint(1, 6)
        print("You rolled:", dice1, dice2)
    elif Q.lower() == "n":
        print("Thanks for playing!")
        break
    else:
        print("Please enter a valid option (Y/N).")
