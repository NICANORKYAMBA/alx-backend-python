#!/usr/bin/env python3
"""Defines a type-annotation for a function."""
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    Returns a tuple of a key and a value.

    Args:
        k (str): key.
        v (Union[int, float]): value.

    Returns:
        tuple[str, float]: key and value.
    """
    return (k, v ** 2)
