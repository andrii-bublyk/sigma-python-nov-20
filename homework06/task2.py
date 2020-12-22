import logging
import time
from functools import wraps

logging.basicConfig(filename="task2_log.log", level=logging.INFO)


def func_logger(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        logging.info(f"function '{func.__name__}' was called with arguments: "
                     f"args{args}, kwargs={kwargs}")

        start_time = time.time()
        result = func(*args, **kwargs)

        run_time = time.time() - start_time
        logging.info(f" function completed in {round(run_time * 1000, 2)} ms\n")

        return result
    return wrapper


@func_logger
def my_func(sleep_time: float, **kwargs):
    time.sleep(sleep_time)
    print(f"function was slept for {sleep_time} sec")


my_func(0.5, one="1", two="2")
my_func(0.2)
my_func(0.8)
