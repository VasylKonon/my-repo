num = input('Enter digit: ')

try:
    num = float(num)
except ValueError as e:
    print(e)
    print('Not a number')
else:
    num = int(num)
    print(num)
