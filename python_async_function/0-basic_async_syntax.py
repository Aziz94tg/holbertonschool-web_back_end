#!/usr/bin/env python3
"""
This module provides an asynchronous coroutine that waits for a random delay
between 0 and max_delay seconds, and then returns that delay.
"""

import asyncio
import random
from typing import Union


async def wait_random(max_delay: int = 10) -> float:
    """
    Asynchronous coroutine that waits for a random delay (float) between
    0 and max_delay seconds and returns the actual delay.

    Args:
        max_delay (int): Maximum number of seconds to wait. Default is 10.

    Returns:
        float: The actual random delay waited.
    """
    delay: float = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
