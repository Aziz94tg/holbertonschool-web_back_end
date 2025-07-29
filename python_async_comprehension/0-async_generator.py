#!/usr/bin/env python3
"""
This module provides an asynchronous generator that yields
10 random floats between 0 and 10, waiting 1 second between each yield.
"""

import asyncio
import random
from typing import AsyncGenerator


async def async_generator() -> AsyncGenerator[float, None]:
    """
    Asynchronous generator that yields 10 random numbers between 0 and 10.
    Waits 1 second between each yield.

    Yields:
        float: Random number between 0 and 10.
    """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
