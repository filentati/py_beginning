class Dictionary:
    def __init__(self, dictionary):
        self.dict = dictionary

    def __call__(self, key):
        return self.dict.get(key, None)

dictionary = Dictionary({1:2, 2:1, 3:3})
print(dictionary(1))
