#!/usr/bin/env python3
"""
Deletion-resilient hypermedia pagination.
"""

import csv
from typing import Dict, List


class Server:
    """Server class to paginate a database of popular baby names."""

    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None
        self.__indexed_dataset = None

    def dataset(self) -> List[List]:
        """Return cached dataset."""
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]  # Skip header row

        return self.__dataset

    def indexed_dataset(self) -> Dict[int, List]:
        """Return indexed dataset."""
        if self.__indexed_dataset is None:
            dataset = self.dataset()
            self.__indexed_dataset = {
                i: dataset[i] for i in range(len(dataset))
            }
        return self.__indexed_dataset

    def get_hyper_index(self, index: int = None, page_size: int = 10) -> Dict:
        """Return pagination details."""
        dataset = self.indexed_dataset()
        index = 0 if index is None else index
        keys = sorted(dataset.keys())
        assert 0 <= index <= keys[-1]

        focus = [i for i in keys if i >= index and len(focus) < page_size]
        data = [dataset[v] for v in focus]
        next_index = focus[-1] + 1 if len(focus) == page_size else None

        return {
            'index': index,
            'data': data,
            'page_size': len(data),
            'next_index': next_index
        }
