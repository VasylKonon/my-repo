def fibonacci_generator():
    num1 = 0
    yield num1
    num2 = 1
    yield num2
    while True:
        yield num2 + num1
        num1, num2 = num2, num1 + num2


fib_gen = fibonacci_generator()
for i in range(10):
    print(next(fib_gen))
