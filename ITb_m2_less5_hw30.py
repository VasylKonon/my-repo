class DictKeysIterator:
    def __init__(self, some_dict):
        self.some_dict = some_dict
        self.num = 0

    def __iter__(self):
        return self

    def __next__(self):
        keys_from_dict = list(self.some_dict.keys())
        if self.num > len(keys_from_dict) - 1:
            raise StopIteration
        else:
            key_from_dict = keys_from_dict[self.num]
            self.num += 1
            return key_from_dict


dictionary = {"a": 1, "b": 2, "c": 3, "d": 4}
dict_iter = DictKeysIterator(dictionary)
for key in dict_iter:
    print(key)
