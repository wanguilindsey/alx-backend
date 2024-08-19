#!/usr/bin/env python3
"""
Defines a function named `index_range`.
"""

from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
    Calculate the start and end index for pagination.

    Args:
        page (int): The current page number.
        page_size (int): The number of items per page.

    Returns:
        Tuple[int, int]: A tuple containing the start and end index.
    """
    next_page_start_index = page * page_size
    return next_page_start_index - page_size, next_page_start_index
