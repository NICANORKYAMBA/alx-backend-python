#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon July  10 14:00:00 2023

@Author: Nicanor Kyamba
"""
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """
    Waits for max_delay seconds and returns a
    random number between 0 and max_delay
    """
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
