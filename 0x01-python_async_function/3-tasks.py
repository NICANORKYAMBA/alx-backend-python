#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon July 10 15:00:00 2023

@Author: Nicanor Kyamba
"""
import asyncio
wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """Task to sleep for random seconds"""
    return asyncio.create_task(wait_random(max_delay))
