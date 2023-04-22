some_list = []


def decorator(func):
    def inner(*args, **kwargs):
        reg = False
        while not reg:
            name = input('Enter your name: ')
            pas = input('Enter your pass')
            if (name, pas) in some_list:
                reg = True
            else:
                print('Invalid name or pass')
        return func(*args, **kwargs)
    return inner
