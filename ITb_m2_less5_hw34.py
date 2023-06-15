class PalindromeIterator:
    def __init__(self, some_list):
        self.some_list = some_list
        self.num = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.num >= len(self.some_list):
            raise StopIteration
        else:
            num = self.num
            self.num += 1
            if self.some_list[num] == self.some_list[num][::-1]:
                return self.some_list[num]
            else:
                return next(self)


words_list = ['level', 'racecar', 'python', 'madam']
palindrome_iter = PalindromeIterator(words_list)
for word in palindrome_iter:
    print(word)
