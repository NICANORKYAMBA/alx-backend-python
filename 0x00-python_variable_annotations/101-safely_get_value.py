#!/usr/bin/python3
"""Defines a type-annotate a function."""
from typing import TypeVar, Mapping, Any, Union

T = TypeVar('T')


def safely_get_value(
        dct: Mapping,
        key: Any,
        default: Union[T, None] = None) -> Union[Any, T]:
    """
    Returns a value from a dictionary.

    Args:
        dct (Mapping): dictionary.
        key (Any): key.

    Returns:
        Union[T, Any]: value.
    """
    if key in dct:
        return dct[key]
    else:
        return default
