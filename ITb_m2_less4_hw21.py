def log_func(func):
    def inner():
        print("Hello")
        func()
        print("Bye")
    return inner


@log_func
def print_work():
    print("work")


print_work()
