def decorator(func):
    counter = 0

    def inner():
        nonlocal counter
        counter += 1
        return counter

    return inner


@decorator
def say_hi():
    print('Hi')


print(say_hi())
print(say_hi())
print(say_hi())
print(say_hi())

