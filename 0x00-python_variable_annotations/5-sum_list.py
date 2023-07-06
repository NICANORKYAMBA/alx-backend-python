#!/usr/bin/env python3
"""Defines type-annotated function."""
from typing import List


def sum_list(input_list: List[float]) -> float:
    """Sum list.

    Args:
        input_list (list): list of numbers.

    Returns:
        float: sum of numbers.
    """
    return sum(input_list)
