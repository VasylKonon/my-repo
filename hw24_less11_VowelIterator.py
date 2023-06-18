class VowelIterator:
    def __init__(self, some_word):
        self.some_word = some_word
        self.i = 0

    def __iter__(self):
        return self

    def __next__(self):
        while len(self.some_word) > self.i:
            w = self.some_word[self.i]
            self.i += 1
            if w.lower() in "aeiouy":
                return w
        raise StopIteration


word = "Hello world"
vowels = VowelIterator(word)
for vowel in vowels:
    print(vowel)
