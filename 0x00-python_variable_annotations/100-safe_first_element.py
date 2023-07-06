#!/usr/bin/env python3
"""

This module contains a code with the correct duck-typed annotations

"""
from typing import Any, Sequence, Union


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """

    Args:
      lst: A sequence of any elements

    Returns:
         Any element or NoneType

    """
    if lst:
        return lst[0]
    else:
        return None
