#!/usr/bin/env python3
"""This python module file contains a measure_runtime coroutine that will execute async_comprehension four times in parallel 
using asyncio.gather.to measure the execution time"""
import time
import asyncio
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """
    measure_runtime - function execute async_com 4 times
    Arguments:
        nothing
    Returns:
        the total exection time required to complete the task
    """
    t_start = time.perf_counter()
    task = [async_comprehension() for i in range(4)]
    await asyncio.gather(*task)
    t_end = time.perf_counter()
    return (t_end - t_start)
