num = input('Enter digit: ')

try:
    num = float(num)
    print(num)
except ValueError as e:
    print(e)
    print('Not a number')
except Exception as e:
    print(e)
    print('Error')
