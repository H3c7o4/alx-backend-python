#!/usr/bin/env python3
"""

This module contains a type-annotated function sum_mixed_list
which takes a list mxd_lst of integers and floats and
returns their sum as a float.

"""
from typing import Union, List


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """

    Args:
      mxd_lst: list of integers and floats

    Returns:
         The sum of the list of integers and floats
    """
    return sum(mxd_lst)
