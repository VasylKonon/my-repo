num1, num2 = int(input('Enter first number: ')), int(input('Enter second number: '))

try:
    res = num1 / num2
except ZeroDivisionError:
    print('You cant divide by 0')
except Exception as e:
    print(e)
    print('Unknown problem')
else:
    print(res)
