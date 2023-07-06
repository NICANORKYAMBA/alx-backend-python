#!/usr/bin/env python3
"""Defines a type-annotation function."""
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """
    Sum list.

    Args:
        mxd_lst (list): list of numbers.

    Returns:
        float: sum of numbers.
    """
    return sum(mxd_lst)
