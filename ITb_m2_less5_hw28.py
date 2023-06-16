class StringIterator:
    def __init__(self, some_str):
        self.some_str = some_str
        self.symbol = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.symbol > len(self.some_str):
            raise StopIteration
        else:
            next_symbol = self.some_str[self.symbol]
            self.symbol += 1
            return next_symbol


string = "Hello, World!"
str_iter = StringIterator(string)
for char in str_iter:
    print(char)
