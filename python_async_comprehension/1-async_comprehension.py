#!/usr/bin/env python3
"""
This module defines an asynchronous coroutine that collects
10 random numbers from an async generator using async comprehension.
"""

from typing import List
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """
    Collect 10 random numbers using an async comprehension
    over the async_generator and return them as a list.

    Returns:
        List[float]: List of 10 random numbers.
    """
    return [number async for number in async_generator()]
