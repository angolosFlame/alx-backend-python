#!/usr/bin/env python3
"""From the previous file, wait_n is imported into 2-measure_runtime.py.
Create a measure_time function with integers n and max_delay as arguments that measures 
the total execution time for wait_n(n, max_delay), and returns total_time / n. 
Your function should return a float."""
from time import perf_counter
import asyncio
wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """Measure the total execution time of a function
    Args:
        n: the number of coroutines to launch
        max_delay: the maximum amount of time to wait for each coroutine
    Returns: elapsed time in seconds
    """
    start = perf_counter()
    asyncio.run(wait_n(n, max_delay))
    elapsed = perf_counter() - start
    return elapsed / n
