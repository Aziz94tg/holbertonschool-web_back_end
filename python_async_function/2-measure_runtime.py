#!/usr/bin/env python3
"""
This module measures the average execution time of calling
the `wait_n` coroutine multiple times concurrently.
"""

import time
import asyncio
from typing import Union
wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """
    Measure the average runtime per task when running `wait_n(n, max_delay)`.

    Args:
        n (int): Number of coroutines to run.
        max_delay (int): Maximum delay for each coroutine.

    Returns:
        float: The average time (in seconds) per coroutine.
    """
    start = time.time()

    asyncio.run(wait_n(n, max_delay))

    end = time.time()
    total_time = end - start
    return total_time / n
