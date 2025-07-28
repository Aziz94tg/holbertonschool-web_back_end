#!/usr/bin/env python3
"""
This module defines a function `make_multiplier` that takes a float as an
argument and returns a function. The returned function multiplies a given
float by the specified multiplier.
"""

from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    Returns a function that multiplies a float by the given multiplier.

    Args:
        multiplier (float): The number to multiply by.

    Returns:
        Callable[[float], float]: A function that takes a float and returns
        the product as a float.
    """
    def multiplier_function(value: float) -> float:
        """Multiplies the given float by the multiplier."""
        return value * multiplier

    return multiplier_function
