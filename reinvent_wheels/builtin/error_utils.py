"""
A minimal `retry` decorator, reinvented instead of depending on a 3rd party
lib such as `tenacity` or `retrying`.
"""
import logging
from functools import wraps
from time import sleep

logger = logging.getLogger(__name__)


def retry(errors: tuple = (Exception,), tries: int = 3, delay: float = 1):
    """Retries the decorated function up to `tries` times when it raises one
    of `errors`, waiting `delay` seconds between attempts. Re-raises the last
    exception once attempts are exhausted.
    """
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            last_error = None
            for attempt in range(1, tries + 1):
                try:
                    return func(*args, **kwargs)
                except errors as e:
                    last_error = e
                    logger.warning(f'{func.__name__} failed on attempt {attempt}/{tries}: {e}')
                    if attempt < tries:
                        sleep(delay)
            raise last_error
        return wrapper
    return decorator
