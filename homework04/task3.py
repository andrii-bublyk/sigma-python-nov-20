def get_alnum_words(s: str) -> list:
    res_list = []
    lst = s.split(' ')
    for word in lst:
        if not word.isdigit() and not word.isalpha():
            res_list.append(word)

    return res_list


print(get_alnum_words("Dash100 apps are rendered in the web3 browser55"))
