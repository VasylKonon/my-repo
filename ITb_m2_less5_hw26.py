def even_odd_generator(n):
    for i in range(1, n + 1):
        if i % 5 == 0 and i % 3 == 0:
            yield "FizzBuzz"
        elif i % 5 == 0:
            yield "Buzz"
        elif i % 3 == 0:
            yield "Fizz"
        else:
            yield i


for el in even_odd_generator(10):
    print(el)
