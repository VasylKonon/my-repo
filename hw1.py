user_pass = input('Enter your password: ')
count = 0


def len_pass(a):
    if len(a) < 12:
        return False
    else:
        return True


def is_upper(b):
    for i in b:
        if i.isupper():
            return True
    else:
        return False


def is_regular(c):
    for i in c:
        if i.islower() and i.isalpha():
            return True
    else:
        return False


def is_digit(d):
    for i in d:
        if i.isdigit():
            return True
    else:
        return False


def is_space(e):
    for i in e:
        if i == ' ':
            return False
    else:
        return True


while count != 5:
    count = 0
    if len_pass(user_pass) is False:
        print('Password validation error. Password must be at least 12 characters long.')
        user_pass = input('Enter your password: ')
    else:
        count += 1

    if is_upper(user_pass) is False:
        print('Password validation error. There must be at least one capital letter')
        user_pass = input('Enter your password: ')
    else:
        count += 1

    if is_regular(user_pass) is False:
        print('Password validation error. There must be at least one regular letter')
        user_pass = input('Enter your password: ')
    else:
        count += 1

    if is_digit(user_pass) is False:
        print('Password validation error. There must be at least one number')
        user_pass = input('Enter your password: ')
    else:
        count += 1

    if is_space(user_pass) is False:
        print('Password validation error. Password must not contain spaces')
        user_pass = input('Enter your password: ')
    else:
        count += 1

else:
    print('successful')
