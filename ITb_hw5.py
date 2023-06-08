def division():
    number1 = int(input("Enter first number: "))
    number2 = int(input("Enter second number: "))
    try:
        res = number1 / number2
    except ZeroDivisionError:
        return "You cant divide by zero."
    else:
        return res


print(division())
