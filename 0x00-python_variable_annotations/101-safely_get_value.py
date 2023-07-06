#!/usr/bin/env python3
"""

This module contains a function

"""
from typing import Any, Mapping, TypeVar, Union
T = TypeVar('T')


def safely_get_value(
        dct: Mapping,
        key: Any,
        default: Union[T, None] = None
        ) -> Union[Any, T]:
    """

    Args:
      dct:
      key:
      default:

    Returns:
        Any element or element of type T
    """
    if key in dct:
        return dct[key]
    else:
        return default
