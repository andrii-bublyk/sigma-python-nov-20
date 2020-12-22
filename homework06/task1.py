from functools import wraps


def calls_counter(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        wrapper.counter += 1
        print(f"\nfunction '{func.__name__}' called {wrapper.counter} times")
        return result

    wrapper.counter = 0
    return wrapper


@calls_counter
def my_func():
    print("hello from my_func")


my_func()
my_func()
my_func()
my_func()
