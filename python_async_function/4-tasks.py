#!/usr/bin/env python3
"""
This module contains a function that uses tasks instead of coroutines directly.
"""

import asyncio
from typing import List
from importlib import import_module

task_wait_random = import_module('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    Spawns task_wait_random n times with the specified max_delay.
    
    Args:
        n (int): Number of tasks to create
        max_delay (int): Maximum delay for each task
        
    Returns:
        List[float]: List of all delays in ascending order
    """
    tasks = [task_wait_random(max_delay) for _ in range(n)]
    
    delays = []
    for task in asyncio.as_completed(tasks):
        delay = await task
        delays.append(delay)
    
    return delays