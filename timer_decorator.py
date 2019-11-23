"""
Title: Timer decorator

A decorator to evaluate the time need to execute a function.
"""

from functools import wraps
import time

def timer(func):
    """A decorator for execution time evaluation.
    """
    @wraps(func)
    def wrapper(*args, **kwargs):
        t_start = time.time()
        result = func(*args, **kwargs)
        t_end = time.time()
        print('\nExecution time: {0}'.format(t_end-t_start))
        return result

    return wrapper
    
@timer
def wait_time(n_sec):
    """Function that wait n_seconds

    Args:
        n_sec (int): Number of seconds to wait
    """
    time.sleep(n_sec)

wait_time(1)

print(wait_time.__doc__)