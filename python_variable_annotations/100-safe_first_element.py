#!/usr/bin/env python3
"""
This module defines a function `safe_first_element` that safely returns
the first element of a sequence, or `None` if the sequence is empty.
It uses duck typing since the element type is not known.
"""

from typing import Sequence, Any, Optional


def safe_first_element(lst: Sequence[Any]) -> Optional[Any]:
    """
    Safely returns the first element of a sequence, or None if empty.

    Args:
        lst (Sequence[Any]): A sequence (like a list, tuple, or string)
            containing elements of any type.

    Returns:
        Optional[Any]: The first element of the sequence, or None if the
        sequence is empty.
    """
    if lst:
        return lst[0]
    return None
