# 1: building a robot barista.

name = input("What is your Name? ")

print("Hello " + name + ", Thank you so much for coming in today!")

menu = "Black coffee, Espresso, Latte, Cappicino."

print(name + ", What would you like from our Menu today?. Here is what we are serving,\n" + menu)

order = input()

print("Sounds good " + name + ", We'll have that " + order + " ready for you in a moment.")



# 2: building a mad libs game.

print('                      Mad Libs\n')
color = input("Enter a color: ")
plural_noun = input("Enter a plural noun: ")
celebrity = input("Enter a celebrity: ")

print("Roses are " + color)
print(plural_noun + " are blue")
print("I love " + celebrity)



# 3: building a basic calculator.

num1 = input("Enter a number: ")
num2 = input("Enter another number: ")

# you can use int instead of float.
result = float(num1) + float(num2)

print(result)
