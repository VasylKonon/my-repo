def memoize(max_size=100):

    def decorator(func):
        my_list = {}

        def inner(*args, **kwargs):
            if args in my_list:
                return my_list[args]
            res = func(*args, **kwargs)
            my_list[args] = res
            return res
        return inner

    return decorator
