#!/usr/bin/env python3
"""
Adds `get_hyper` method to `Server` class.
"""

import csv
from typing import Dict, List, Tuple, Union


class Server:
    """Server class to paginate a database of popular baby names."""

    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset.

        Returns:
            List[List]: The dataset containing lists of baby names.
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]  # Skip header row

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
        """Get items for the given page number.

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

    def get_hyper(
        self, page: int, page_size: int
    ) -> Dict[str, Union[int, List[List], None]]:
        """Get paginated data along with hypermedia pagination info.

        Args:
            page (int): The page number.
            page_size (int): The number of items per page.

        Returns:
            Dict[str, Union[int, List[List], None]]: A dictionary containing:
                - page_size: The size of the current page.
                - page: The current page number.
                - data: The data on the current page.
                - next_page: The next page number, or None if no next page.
                - prev_page: The previous page number,
                or None if no previous page.
                - total_pages: The total number of pages.
        """
        data = self.get_page(page, page_size)
        total_rows = len(self.dataset())
        prev_page = page - 1 if page > 1 else None
        next_page = (
            page + 1
            if self.index_range(page, page_size)[1] < total_rows
            else None
        )
        total_pages = (total_rows + page_size - 1) // page_size

        return {
            'page_size': len(data),
            'page': page,
            'data': data,
            'next_page': next_page,
            'prev_page': prev_page,
            'total_pages': total_pages,
        }
