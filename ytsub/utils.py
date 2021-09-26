import asyncio
import functools


def parse_timestamp(t_str: str) -> float:
    """
    >>> parse_timestamp("00:01:38.970")
    98.97
    """
    h, m, s = t_str.split(":")
    return (int(h) * 60 + int(m)) * 60 + float(s)


def wrap_in_sync(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        return asyncio.run(func(*args, **kwargs))

    return wrapper
