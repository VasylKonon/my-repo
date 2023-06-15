def prime_generator():
    num = 1
    while True:
        y = 0
        for i in range(1, num + 1):
            if num % i == 0:
                y += 1
        if y == 2:
            yield num
        num += 1


prime_gen = prime_generator()
for _ in range(10):
    print(next(prime_gen))
