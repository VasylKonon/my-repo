def retry(num=2):

    def decorator(func):

        def inner(*args, **kwargs):
            print("Hello, lets try this decorator.")
            for i in range(num):
                try:
                    func(*args, **kwargs)
                except Exception:
                    print(f"Wrong input in {i + 1} try")
                else:
                    print("Successfully")
                    return

            print("Shut down")

        return inner

    return decorator


@retry(5)
def input_age():
    age = int(input("How old are you? "))
    print(f"Your age is {age}")


input_age()
