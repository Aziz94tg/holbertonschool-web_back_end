#!/usr/bin/env python3
"""
This module provides an async coroutine `wait_n` that runs `wait_random`
multiple times concurrently and returns the delays in ascending order.
"""

import asyncio
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    Run `wait_random` n times concurrently with the given max_delay.
    Collects and returns all delays in ascending order.

    Args:
        n (int): Number of coroutines to run.
        max_delay (int): Maximum delay for each coroutine.

    Returns:
        List[float]: List of all delay values in ascending order.
    """
    
    tasks = [wait_random(max_delay) for _ in range(n)]

    delays: List[float] = []

    
    for completed_task in asyncio.as_completed(tasks):
        delay = await completed_task

        
        inserted = False
        for i, value in enumerate(delays):
            if delay < value:
                delays.insert(i, delay)
                inserted = True
                break
        if not inserted:
            delays.append(delay)

    return delays
