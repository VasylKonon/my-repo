def debug(print_input=False, print_output=False):
    def decorator(func):
        def inner(*args, **kwargs):
            if print_input:
                print(f"Input: {args}")
            res = func(*args, **kwargs)
            if print_output:
                print(f"Output: {res}")
            return res
        return inner
    return decorator


@debug(print_input=True, print_output=True)
def add(x, y):
    return x+y


result = add(2, 3)
