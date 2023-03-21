filename = 'hw8.txt'

try:
    f = open(filename, 'r')
    file = f.read()
    file_list = file.split()
    num = []
    for i in file_list:
        num.append(int(i))
    res = sum(num)
    print(res)
except FileNotFoundError:
    print('File not found')
except PermissionError:
    print('No permission to the file')
except ValueError:
    print('File contains non-integer values')
finally:
    print('The program is completed')
