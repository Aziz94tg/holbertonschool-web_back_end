#!/usr/bin/env python3
"""
This module defines a coroutine `measure_runtime` that runs
`async_comprehension` four times in parallel and measures total runtime.
"""

import asyncio
import time
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """
    Run `async_comprehension` four times in parallel and
    measure the total runtime.

    Returns:
        float: Total time taken to run the four comprehensions.
    """
    start = time.time()

    await asyncio.gather(*(async_comprehension() for _ in range(4)))

    end = time.time()
    return end - start
