#!/usr/bin/env python3
"""
This module defines a function `element_length` that takes an iterable of
sequences and returns a list of tuples.
Each tuple contains the original element and its length.
"""

from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    Returns a list of tuples with each element from the iterable and its length

    Args:
        lst (Iterable[Sequence]): An iterable containing sequence elements
        (e.g., strings, lists, or tuples).

    Returns:
        List[Tuple[Sequence, int]]: A list where each tuple contains an element
        from the iterable and the length of that element.
    """
    return [(i, len(i)) for i in lst]
