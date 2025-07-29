#!/usr/bin/env python3
"""
This module defines an async function `task_wait_n` that runs multiple
`task_wait_random` tasks concurrently and returns their results in ascending order.
"""

import asyncio
from typing import List
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    Run `task_wait_random` n times concurrently and return the results
    in ascending order without using sort().

    Args:
        n (int): Number of tasks to run.
        max_delay (int): Maximum delay for each task.

    Returns:
        List[float]: Sorted list of all delay values.
    """
    tasks = [task_wait_random(max_delay) for _ in range(n)]
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
