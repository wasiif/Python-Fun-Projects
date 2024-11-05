# Creates a multiplication table for a given number
name = input("Enter your name: ")
num = int(input(f"{name}, enter a number: "))

def tab(num):
    print(f"\nMultiplication Table for {num}:\n")
    for i in range(1, 11):
        print(f"{num} x {i:2} = {num * i}")

tab(num)
