#!/usr/bin/env python3
"""
This module defines a function `safely_get_value` that retrieves a value
from a mapping (like a dictionary). If the key is not found, it returns
a default value. It uses TypeVar for more precise type annotations.
"""

from typing import Mapping, Any, TypeVar, Union

T = TypeVar('T')


def safely_get_value(
        dct: Mapping,
        key: Any,
        default: Union[T, None] = None) -> Union[Any, T]:
    """
    Safely retrieves a value from a mapping by key.

    Args:
        dct (Mapping): The mapping (e.g., dictionary) to look into.
        key (Any): The key to search for.
        default (Union[T, None]): The default value to return if
            the key is not found.

    Returns:
        Union[Any, T]: The value associated with the key if it exists,
        otherwise the default value.
    """
    if key in dct:
        return dct[key]
    return default
