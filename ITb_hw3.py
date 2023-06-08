try:
    number1 = int(input('Enter first number: '))
except ValueError:
    print("Entered not a number.")
else:
    print(f"You first number is {number1}")


try:
    number2 = int(input('Enter second number: '))
except ValueError:
    print("Entered not a number.")
else:
    print(f"You second number is {number2}")
