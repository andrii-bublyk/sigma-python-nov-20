def html_decorator(tag: str, num: int):
    def decorator(func):
        def wrapper(text: str) -> list:
            func(text)

            for ch in ['@', '#', '%', '&', '$', '^', '*', '_']:
                text = text.replace(ch, ' ')

            for ch in ['<', '>', '/']:
                text = text.replace(ch, '')

            text = text.capitalize()

            result = [f"<{tag}>{text} {i}</{tag}>" for i in range(1, num + 1)]
            return result
        return wrapper
    return decorator


@html_decorator("li", 3)
def html_element(text: str):
    pass


print(html_element('>list_item<'))
print(html_element("@lis^&#t_it*_em"))
