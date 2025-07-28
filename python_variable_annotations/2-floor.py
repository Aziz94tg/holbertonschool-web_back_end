#!/usr/bin/env python3
"""
This module defines a function `floor` that takes a float as an argument
and returns its floor value as an integer.
"""

import math


def floor(n: float) -> int:
    """
    Returns the floor of a given float.

    Args:
        n (float): The number to apply the floor function to.

    Returns:
        int: The largest integer less than or equal to the given float.
    """
    return math.floor(n)
