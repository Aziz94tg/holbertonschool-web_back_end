#!/usr/bin/env python3
"""
This module defines a function `sum_list` that takes a list of floats
and returns their sum as a float.
"""

from typing import List


def sum_list(input_list: List[float]) -> float:
    """
    Calculates the sum of a list of floats.

    Args:
        input_list (List[float]): The list of float numbers to sum.

    Returns:
        float: The sum of all numbers in the list.
    """
    return float(sum(input_list))
