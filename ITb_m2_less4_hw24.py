def memoize(func):
    memory_dict = {}

    def inner(*args, **kwargs):
        if args in memory_dict:
            print(memory_dict)
            return memory_dict[args]
        else:
            memory_dict[args] = func(*args)
            print(memory_dict)
            return memory_dict[args]

    return inner


@memoize
def add_func(a, b):
    res = a + b
    return res


print(add_func(10, 10))
print(add_func(2, 10))
print(add_func(22, 2))
print(add_func(1, 1))
print(add_func(10, 10))
print(add_func(10, 2))
