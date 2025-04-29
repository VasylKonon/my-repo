from time import time, sleep
from contextlib import contextmanager


class ContextManager:
    def __enter__(self):
        print("Start")
        self.start = time()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        end = time()
        print("Stop")
        res = end - self.start
        print(f"The program ran for {res} sec")


with ContextManager() as manager:
    print("work...")
    sleep(2)


print("#" * 50)


@contextmanager
def context_manager():
    print("Start")
    start = time()
    yield
    end = time()
    print("Stop")
    print(f"The program ran for {end - start} sec")


with context_manager() as manager2:
    print("work...")
    sleep(2)
