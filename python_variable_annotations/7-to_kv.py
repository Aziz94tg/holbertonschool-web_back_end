#!/usr/bin/env python3
"""
This module defines a function `to_kv` that takes a string and an integer
or float and returns a tuple. The first element is the string, and the
second element is the square of the number as a float.
"""

from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    Returns a tuple with a string and the square of a number as a float.

    Args:
        k (str): The string key.
        v (Union[int, float]): The number to square.

    Returns:
        Tuple[str, float]: A tuple where the first element is the string `k`
        and the second element is `v` squared as a float.
    """
    return (k, float(v ** 2))
