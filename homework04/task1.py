def get_head_and_tail(s: str) -> str:
    if len(s) < 2:
        return ""

    return s[:2] + s[len(s) - 2:]


print(get_head_and_tail("Winter"))
print(get_head_and_tail("r2"))
print(get_head_and_tail("p"))
