def is_error():
    try:
        number1 = int(input('Enter first number: '))
        number2 = int(input('Enter second number: '))
        return f"Your first number is {number1}, your second number is {number2}"
    except ValueError:
        return "Entered not a number."


print(is_error())
