def square_generator(num):
    for i in range(1, num + 1):
        yield i ** 2


for square in square_generator(5):
    print(square)
