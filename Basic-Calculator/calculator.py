# Basic Calculator
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
operator = input("Select an operator (+, -, x, /): ")

def calculate(num1, num2, operator):
    if operator == "+":
        print(f"The sum of {num1} and {num2} is: {num1 + num2}")
    elif operator == "-":
        print(f"The difference of {num1} and {num2} is: {num1 - num2}")
    elif operator == "x":
        print(f"The product of {num1} and {num2} is: {num1 * num2}")
    elif operator == "/":
        if num2 != 0:
            print(f"The division of {num1} by {num2} is: {num1 / num2}")
        else:
            print("Error: Division by zero is undefined.")
    else:
        print("Invalid operator! Please select from +, -, x, /.")

calculate(num1, num2, operator)
