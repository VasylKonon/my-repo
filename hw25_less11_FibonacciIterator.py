class FibonacciIterator:
    def __init__(self, num):
        self.num = num
        self.n1 = 0
        self.n2 = 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.n1 <= self.num:
            n = self.n1
            self.n1, self.n2 = self.n2, self.n1 + self.n2
            return n
        else:
            raise StopIteration


fibonacci = FibonacciIterator(20)
for number in fibonacci:
    print(number)
