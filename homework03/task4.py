def get_palindrome_words_comprehension_method(words: list) -> list:
    palindrome_words = [w for w in words if w == w[::-1]]
    return palindrome_words


def get_palindrome_words_filter_method(words: list) -> list:
    palindrome_words = filter(lambda w: w == w[::-1], words)
    return list(palindrome_words)


words = ["radar", "device", "level", "program", "kayak", "river", "racecar"]

print(get_palindrome_words_comprehension_method(words))
print(get_palindrome_words_filter_method(words))
