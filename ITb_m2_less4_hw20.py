from contextlib import contextmanager


@contextmanager
def divider_context(func):
    print(func * 25)
    yield

    print(func * 25)


with divider_context("-_-") as manager:
    print("hello")


print("\n")
print("|" * 100)
print("\n")


class DividerContext:
    def __init__(self, symbol):
        self.symbol = symbol
        print("initialization")

    def __enter__(self):
        print(self.symbol * 25)
        return self.symbol

    def __exit__(self, exc_type, exc_val, exc_tb):
        print(self.symbol * 25)


with DividerContext("=") as manager2:
    print("hello")
