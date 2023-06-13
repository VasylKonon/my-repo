from time import time, sleep
from contextlib import contextmanager


@contextmanager
def context():
    print("start")
    start = time()
    yield
    end = time()
    print("end")
    print(start - end)


with context() as manager:
    print("work")
    sleep(3)

print("#" * 25)


class Context:
    def __init__(self):
        print("init method called")

    def __enter__(self):
        print("start")
        self.start2 = time()
        return self

    def __exit__(self, exc_type, exc_value, exc_traceback):
        self.end2 = time()
        print("end")
        print(self.start2 - self.end2)


with Context() as manager2:
    print("work")
    sleep(3)
