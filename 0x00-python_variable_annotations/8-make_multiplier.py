#!/usr/bin/env python3
"""Defines a type-annotated function"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    Returns a function that multiplies a float by a number.

    Args:
        multiplier (float): number to multiply.

    Returns:
        Callable[[float], float]: function that multiplies a float by a number.
    """
    def mult(x: float) -> float:
        """
        Function that multiplies a float by a number.

        Args:
            x (float): number to multiply.

        Returns:
            float: x * multiplier.
        """
        return x * multiplier
    return mult
