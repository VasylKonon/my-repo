import time


def timeit(func):
    def inner():
        start = time.time()
        print("start")
        func()
        print("stop")
        stop = time.time()
        print(start - stop)

    return inner


@timeit
def some_work():
    print("some work...")
    time.sleep(2)


some_work()
