#!/usr/bin/env python3
"""
This module defines a function `zoom_array` that takes a tuple and
returns a zoomed-in list by repeating each element based on the factor.
It ensures proper type checking with mypy.
"""

from typing import Tuple, List, Any


def zoom_array(lst: Tuple[Any, ...], factor: int = 2) -> List[Any]:
    """
    Returns a zoomed-in list, where each element of the input tuple
    is repeated `factor` times.

    Args:
        lst (Tuple[Any, ...]): The input tuple.
        factor (int): The repeat factor (default is 2).

    Returns:
        List[Any]: A list with elements repeated based on the factor.
    """
    zoomed_in: List[Any] = [
        item for item in lst for _ in range(factor)
    ]
    return zoomed_in


array: Tuple[int, ...] = (12, 72, 91)

zoom_2x = zoom_array(array)

zoom_3x = zoom_array(array, 3)
