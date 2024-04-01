#!/usr/bin/env python3
"""
returns a tuple containing start and end index
"""
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """ function that return start and end index """
    return ((page - 1) * page_size, page * page_size)
