#!/usr/bin/env python3
"""
This module defines a function `sum_mixed_list` that takes a list of integers
and floats and returns their sum as a float.
"""

from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """
    Calculates the sum of a list containing both integers and floats.

    Args:
        mxd_lst (List[Union[int, float]]): The list of integers and floats to sum.

    Returns:
        float: The sum of all elements in the list.
    """
    return float(sum(mxd_lst))
