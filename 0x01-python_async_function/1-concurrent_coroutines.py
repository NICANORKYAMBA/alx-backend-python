#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon July 10 14:30:00 2023

@Author: Nicanor Kyamba
"""
import asyncio
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> list:
    """
    Wait n seconds and return the delay.
    """
    delays = []
    tasks = []

    for _ in range(n):
        task = asyncio.create_task(wait_random(max_delay))
        tasks.append(task)

    for task in tasks:
        delay = await task
        delays.append(delay)

    return sorted(delays)
