#!/usr/bin/env python3
"""Defines ducktyping annotations function."""
from typing import Sequence, Any, Union


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """
    Function that returns the first element of a list.

    Args:
        lst (Sequence[Any]): list.

    Returns:
        Union[Any, Optional[None]]: first element of a list.
    """
    if lst:
        return lst[0]
    else:
        return None
