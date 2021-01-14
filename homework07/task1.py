import itertools as it


class Sentense:
    def __init__(self, sentence: str):
        self.current_index = 0
        self.words = sentence.split(' ')

    def __iter__(self):
        return self

    def __next__(self):
        if self.current_index >= len(self.words):
            raise StopIteration

        current_value = self.words[self.current_index]
        self.current_index += 1
        return current_value


sentence1 = Sentense("one two three four five")
for word in sentence1:
    print(word)

print()

sentence2 = Sentense("one two three")
counter = it.count()
for i in counter:
    try:
        print(next(sentence2))
    except StopIteration:
        print("iteration has been finished")
        break
