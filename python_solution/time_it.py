import time
from functools import wraps


def time_it(func):  # This is the decorator function
    """
    Decorator that measures the execution time of a function.
    """
    @wraps(func)  # Preserve the original function's metadata
    def wrapper(*args, **kwargs):
        start_time = time.perf_counter()  # Record the start time
        result = func(*args, **kwargs)   # Call the original function
        end_time = time.perf_counter()    # Record the end time
        execution_time = end_time - start_time  # Calculate the elapsed time

        # print time taken in ms
        # print(f"Function '{func.__name__}' took {execution_time:.12f} seconds to execute.")

        # print time taken in ms
        ms = execution_time*1000
        print(f"Function '{func.__name__}' took \033[35m{ms:.12f}\033[0m ms to execute.")

        return result
    return wrapper
