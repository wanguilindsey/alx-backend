#!/usr/bin/env python3
"""
Adds `get_page` method to `Server` class.
"""

import csv
from typing import List, Tuple


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    @staticmethod
    def index_range(page: int, page_size: int) -> Tuple[int, int]:
        """Calculate start and end index range for a page, with page_size.

        Args:
            page (int): The current page number.
            page_size (int): The number of items per page.

        Returns:
            Tuple[int, int]: The start and end index for the given page.
        """
        next_page_start_index = page * page_size
        return next_page_start_index - page_size, next_page_start_index

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """
        Get items for the given page number.

        Args:
            page (int): The page number.
            page_size (int): The number of items per page.

        Returns:
            List[List]: A list of rows corresponding to the given page.
            []: An empty list if the page or page_size is out of range.
        """
        assert isinstance(page, int) and isinstance(page_size, int), \
            "Page and page_size must be integers."
        assert page > 0 and page_size > 0, \
            "Page and page_size must be greater than 0."

        start_index, end_index = self.index_range(page, page_size)
        return self.dataset()[start_index:end_index]
