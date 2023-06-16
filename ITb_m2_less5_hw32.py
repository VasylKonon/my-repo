class EvenRangeIterator:
    def __init__(self, start_range, end_range):
        self.start_range = start_range
        self.end_range = end_range

    def __iter__(self):
        return self

    def __next__(self):
        if self.start_range > self.end_range:
            raise StopIteration
        else:
            start = self.start_range
            self.start_range += 1
            if start % 2 == 0:
                return start
            else:
                return next(self)


even_nums = EvenRangeIterator(1, 10)
for num in even_nums:
    print(num)
