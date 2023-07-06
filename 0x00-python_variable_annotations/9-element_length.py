#!/usr/bin/env python3
"""Defines a type annotation function."""
from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    Returns a list of tuples containing the element and its length.

    Args:
        lst (Iterable[Sequence]): iterable.

    Returns:
        List[Tuple[Sequence, int]]: list of tuples.
    """
    return [(i, len(i)) for i in lst]
