#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue July 11 12:30:00 2023

@Author: Nicanor Kyamba
"""
import asyncio
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """Measure the runtime of async_comprehension"""
    start_time = asyncio.get_event_loop().time()

    await asyncio.gather(
        async_comprehension(),
        async_comprehension(),
        async_comprehension(),
        async_comprehension()
        )

    end_time = asyncio.get_event_loop().time()

    total_time = end_time - start_time
    return total_time
