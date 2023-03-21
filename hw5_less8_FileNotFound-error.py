filename = input('Enter file name: ')              # hw5.txt

try:
    f = open(filename, 'r')
except FileNotFoundError as e:
    print(e)
    print('Not found')
except Exception as e:
    print(e)
    print('Unknown error')
else:
    print(f.read())
    f.close()
