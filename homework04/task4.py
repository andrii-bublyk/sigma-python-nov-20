def save_and_get_binary_presentation(path: str, in_str: str) -> list:
    byte_presentation = bytes(in_str, encoding="utf-8")

    with open(path, "wb") as f:
        f.write(byte_presentation)

    with open(path, "rb") as f:
        data = f.read()

    return list(data)


print(save_and_get_binary_presentation("test.txt", "Hello Python"))
