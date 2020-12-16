def replace_with_first_char(s: str) -> str:
    if len(s) < 2:
        return s

    c = s[0]
    s = s[0] + s[1:].replace(c, '_')
    return s


print(replace_with_first_char("abracadabra"))
