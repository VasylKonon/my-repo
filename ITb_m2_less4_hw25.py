import time


def rate_limit(max_calls, period):
    def decorator(func):
        def inner():
            s = period
            for i in range(max_calls):
                if s <= 0:
                    return
                start = time.time()
                func()
                end = time.time()
                res = end - start
                s -= res

        return inner

    return decorator


@rate_limit(5, 10)
def my_function():
    print("This function is rate-limited!")
    time.sleep(5)


my_function()
