#!/usr/bin/env python3
"""

This module contains a function that return an iterable

"""
from typing import Iterable, List, Sequence, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """

    Args:
      lst: An Iterable of Sequences

    Return:
       A list of tuples
    """
    return [(i, len(i)) for i in lst]
