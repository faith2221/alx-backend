#!/usr/bin/env python3
"""
Pagination that deals with indexes.
"""
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """Returns start index and end index as a tuple."""
    start_index = (page - 1) * page_size
    end_index = page * page_size

    return (start_index, end_index)
