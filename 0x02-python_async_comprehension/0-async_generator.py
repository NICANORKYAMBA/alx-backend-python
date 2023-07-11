#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue 11 11:00:00 2023

@Author: Nicanor Kyamba
"""
import random
import asyncio
from typing import AsyncGenerator


async def async_generator() -> AsyncGenerator[float, None]:
    """
    Async generator
    """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
