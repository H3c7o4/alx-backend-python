#!/usr/bin/env python3
"""

This module contains a type-annotated function sum_list
which takes a list input_list of floats as argument and
returns their sum as a float.

"""
from typing import List


def sum_list(input_list: List[float]) -> float:
    """

    Args:
       input_list: list of floats

    Returns:
        The sum of the floats inside a list
    """
    return sum(input_list)
