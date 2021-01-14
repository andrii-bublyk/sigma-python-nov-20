def word_generator(sentence: str):
    """
    Return words from the sentence until it is exhausted.
    :param sentence: input sentence
    :return: words generator
    """
    words = sentence.split(' ')
    current_index = 0

    while current_index < len(words):
        yield words[current_index]
        current_index += 1


sentence = "one two three four five"

# generator function
word_gen = word_generator(sentence)
for word in word_gen:
    print(word)

print()

# generator expression
word_gen = (word for word in sentence.split(' '))
for word in word_gen:
    print(word)
